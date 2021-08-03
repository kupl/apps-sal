import numpy as np

N, M = map(int, input().strip().split())
PY = np.array([list(map(int, input().strip().split())) for _ in range(M)])

l = [[] for n in range(N)]
for m in range(M):
    l[PY[m, 0] - 1].append(PY[m, 1])

dp = {}
for n in range(N):
    if l[n]:
        l[n].sort()
        for i in range(len(l[n])):
            city = "000000" + str(n + 1)
            num = "000000" + str(i + 1)
            dp[(n, l[n][i] - 1)] = str(city[-6:] + num[-6:])
for m in range(M):
    print(dp[(PY[m, 0] - 1, PY[m, 1] - 1)])
