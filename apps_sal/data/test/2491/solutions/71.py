def bellman_ford(s):
    d = [float('inf')] * (N + 1)
    d[s] = 0
    nega = [0 for i in range(N + 1)]
    for i in range(N + 1):
        update = False
        for (x, y, z) in g:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True
                nega[y] += 1
        if not update:
            break
        if i == N:
            d[0] = -1
    return [d, nega]


(N, M) = map(int, input().split())
g = []
for _ in range(M):
    (x, y, z) = [int(x) for x in input().split()]
    g.append([x, y, -z])
ans = bellman_ford(1)
if ans[1][-1] > 1:
    print('inf')
else:
    print(int(-ans[0][-1]))
