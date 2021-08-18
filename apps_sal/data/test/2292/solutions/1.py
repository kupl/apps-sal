from collections import deque


def Hopcroft_Karp(adj, L):
    """
    Computes maximal matching in unweighted bipartite graph `adj`. Here `L` is
    a boolean array which gives the left part of the bipartite graph. If w is
    in adj[v], then precisely one of L[v], L[w] should be True.

    Returns (N, matching), where N is the cardinality of the matching, and
    matching is a list encoding the matched vertex (where a -1 indicates an
    unmatched vertex).
    """
    N = len(adj)
    matching = [-1 for _ in range(N)]

    while True:
        extended = False

        sources = [v for v in range(N) if matching[v] == -1 and L[v]]

        bfs_pred = [-1 for _ in range(N)]

        bfs_source = [-1 for _ in range(N)]

        for v in sources:
            bfs_pred[v] = v
            bfs_source[v] = v

        queue = deque(sources)
        while len(queue) > 0:
            cur = queue.popleft()

            if matching[bfs_source[cur]] != -1:
                continue

            for nb in adj[cur]:
                if matching[nb] == -1:
                    while nb != -1:
                        matching[nb], matching[cur], nb, cur = cur, nb, matching[cur], bfs_pred[cur]
                    extended = True
                    break
                else:
                    new = matching[nb]
                    if bfs_pred[new] == -1:
                        bfs_pred[new] = cur
                        bfs_source[new] = bfs_source[cur]
                        queue.append(new)
        if not extended:
            break

    return sum(1 for x in matching if x != -1) // 2, matching


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    if n % 2:
        if a[n // 2] != b[n // 2]:
            print("No")
            continue

    a_pairs = []
    b_pairs = []
    for i in range(n // 2):
        if a[i] < a[n - i - 1]:
            a_pairs.append((a[i], a[n - i - 1]))
        else:
            a_pairs.append((a[n - i - 1], a[i]))
        if b[i] < b[n - i - 1]:
            b_pairs.append((b[i], b[n - i - 1]))
        else:
            b_pairs.append((b[n - i - 1], b[i]))

    adj = [[] for _ in range(len(a_pairs) + len(b_pairs))]
    for i, ap in enumerate(a_pairs):
        for j, bp in enumerate(b_pairs):
            if ap == bp:
                adj[i].append(len(a_pairs) + j)
                adj[len(a_pairs) + j].append(i)

    if Hopcroft_Karp(adj, [True] * len(a_pairs) + [False] * len(b_pairs))[0] == len(a_pairs):
        print("Yes")
    else:
        print("No")
