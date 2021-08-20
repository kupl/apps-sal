(N, M) = map(int, input().split())
Std = [tuple(map(int, input().split())) for _ in range(N)]
Chp = [tuple(map(int, input().split())) for _ in range(M)]
INF = 10000000000.0
Arrv = []


def Mdist(x, y, u, v):
    return abs(x - u) + abs(y - v)


for s in Std:
    close = INF
    for i in range(M):
        dist = Mdist(*s, *Chp[i])
        if dist < close:
            close = dist
            arrv = i + 1
    Arrv.append(arrv)
for ar in Arrv:
    print(ar)
