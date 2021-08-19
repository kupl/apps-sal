import sys
(n, m) = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))
T = list(map(int, sys.stdin.readline().split()))
Taxi = []
Res = []
for i in range(n + m):
    if T[i] == 1:
        Taxi.append(X[i])
    else:
        Res.append(X[i])
TMAP = [[0, 0] for i in range(m)]
for i in range(m - 1):
    TMAP[i][1] = (Taxi[i] + Taxi[i + 1]) // 2
    TMAP[i + 1][0] = (Taxi[i] + Taxi[i + 1]) // 2 + 1
TMAP[m - 1][1] = X[-1]
TCOUNT = [0 for i in range(m)]
i = 0
for j in Res:
    while True:
        if TMAP[i][0] <= j <= TMAP[i][1]:
            TCOUNT[i] += 1
            break
        else:
            i += 1
for t in TCOUNT:
    print(t, end=' ')
