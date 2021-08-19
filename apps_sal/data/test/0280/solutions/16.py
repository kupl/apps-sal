from itertools import permutations
from bisect import *
(N, M) = list(map(int, input().split()))
w = list(map(int, input().split()))
lv = [list(map(int, input().split())) for _ in range(M)]
w.sort()
lv.sort(key=lambda x: x[1])
seq = list(range(N))
x = list(permutations(seq))
vs = [0]
ls = [0]
ans = float('inf')
ma = 0
flag = 1
for i in range(M):
    ma = max(ma, lv[i][0])
    vs.append(lv[i][1])
    ls.append(ma)
for i in range(N):
    if w[i] > lv[0][1]:
        flag = 0
for tuples in x:
    cuml = [0]
    buf = 0
    for i in tuples:
        buf = buf + w[i]
        cuml.append(buf)
    disttable = [[0] * N for _ in range(N)]
    dist = [0] * N
    for i in range(N + 1):
        for j in range(i + 2, N + 1):
            weight = cuml[j] - cuml[i]
            ind = bisect_left(vs, weight)
            disttable[i][j - 1] = ls[ind - 1]
    for i in range(N):
        for j in range(i + 1, N):
            dist[j] = max(dist[j], dist[i] + disttable[i][j])
    ans = min(ans, dist[N - 1])
if flag == 1:
    print(ans)
else:
    print(-1)
