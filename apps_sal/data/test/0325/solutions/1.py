import sys
from collections import deque
input = sys.stdin.readline


def belman(egdes, N, start, end):
    INF = int(10000000000.0)
    cost = [INF] * N
    cost[start] = 0
    fin = False
    count = 0
    while True:
        no_change = True
        for edge in egdes:
            (from_, to_, d) = edge
            tmp = cost[from_] + d
            if cost[to_] > tmp:
                no_change = False
                cost[to_] = tmp
        count += 1
        if no_change:
            fin = True
            break
        elif count > N + 1:
            break
    if fin:
        return max(0, -cost[end])
    else:
        return -1


def bfs(link, N, start):
    q = deque()
    check = [False] * N
    q.append(start)
    check[start] = True
    used = {start}
    while len(q) > 0:
        node = q.popleft()
        for next_ in link[node]:
            if not check[next_]:
                check[next_] = True
                q.append(next_)
                used.add(next_)
    return used


def main():
    (N, M, P) = map(int, input().split())
    link = [[] for i in range(N)]
    rlink = [[] for i in range(N)]
    edges = []
    for i in range(M):
        (a, b, c) = map(int, input().split())
        a -= 1
        b -= 1
        link[a].append(b)
        rlink[b].append(a)
        edges.append((a, b, -(c - P)))
    use_nodes = bfs(link, N, 0) & bfs(rlink, N, N - 1)
    use_edges = [(a, b, c) for (a, b, c) in edges if a in use_nodes and b in use_nodes]
    print(belman(use_edges, N, 0, N - 1))


def __starting_point():
    main()


__starting_point()
