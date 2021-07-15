from heapq import heapify, heappush, heappop


def solve():
    n, m = [int(x) for x in input().split()]

    adjs = [[] for _ in range(n)]
    for _ in range(m):
        a, b = [int(x) for x in input().split()]
        a -= 1
        b -= 1
        adjs[a].append(b)
        adjs[b].append(a)

    seq = [1]
    visited = set([0])
    frontier = adjs[0].copy()
    heapify(frontier)

    while frontier:
        node = heappop(frontier)
        if node in visited:
            continue

        seq.append(node+1)
        visited.add(node)
        for neighbor in adjs[node]:
            if neighbor not in visited:
                heappush(frontier, neighbor)

    print(*seq)


solve()

