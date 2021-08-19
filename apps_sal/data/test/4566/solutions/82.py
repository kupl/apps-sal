from collections import defaultdict
(n, m) = map(int, input().split())
ans = 0
route = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    (f, t) = map(int, input().split())
    route[f][t] += 1
    route[t][f] += 1
for i in range(1, n + 1):
    print(sum(route[i]))
