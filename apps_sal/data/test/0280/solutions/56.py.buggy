import bisect
from itertools import permutations

N, M = map(int, input().split())
w = list(map(int, input().split()))

bridge = []
for i in range(M):
    l, W = map(int, input().split())
    bridge.append((W, l))
bridge.sort()

if min(bridge[i][0] for i in range(M)) < max(w):
    print(-1)
    return()

Max = [bridge[i][1] for i in range(M)]
for i in range(1, M):
    Max[i] = max(Max[i], Max[i - 1])

data = [0 for i in range(2**N)]

for i in range(2**N):
    tmp = 0
    for j in range(N):
        if i >> j & 1:
            tmp += w[j]

    idx = bisect.bisect_left(bridge, (tmp, -1))
    if idx == 0:
        data[i] = 0
    else:
        data[i] = Max[idx - 1]

per = list(permutations([i for i in range(N)]))
res = 10**18
for L in per:
    d = [0 for i in range(N)]
    for i in range(1, N):
        tmp = 1 << L[i]
        for j in range(i - 1, -1, -1):
            tmp += 1 << L[j]
            d[i] = max(d[i], data[tmp] + d[j])
    res = min(res, d[-1])

print(res)
