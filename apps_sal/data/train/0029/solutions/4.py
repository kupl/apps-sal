t = int(input())
for case in range(t):
    n = int(input())
    a = [int(x) - 1 for x in input().split()]
    last_occ = [-1 for _ in range(n)]
    max_dist = [float('-inf') for _ in range(n)]
    for (i, x) in enumerate(a):
        max_dist[x] = max(max_dist[x], i - last_occ[x])
        last_occ[x] = i
    for x in a:
        max_dist[x] = max(max_dist[x], n - last_occ[x])
    inverted = [float('inf') for _ in range(n)]
    for x in a:
        inverted[max_dist[x] - 1] = min(inverted[max_dist[x] - 1], x)
    best = float('inf')
    for x in inverted:
        if x != float('inf'):
            best = min(x, best)
        if best == float('inf'):
            print(-1, end=' ')
        else:
            print(best + 1, end=' ')
    print()
