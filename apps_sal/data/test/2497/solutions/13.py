import sys
input = sys.stdin.readline

INF = 10**18

N = int(input())
D = []
U = []
L = []
R = []
UD = []
LR = []
for _ in range(N):
    str_x, str_y, d = map(str, input().rstrip().split())
    x = int(str_x)
    y = int(str_y)
    if d == "U":
        U.append(y)
        UD.append(x)
    elif d == "D":
        D.append(y)
        UD.append(x)
    elif d == "L":
        L.append(x)
        LR.append(y)
    else:
        R.append(x)
        LR.append(y)

UD.sort()
LR.sort()
U.sort()
D.sort()
L.sort()
R.sort()

T = [0]
if L and R:
    T.append((L[0] - R[0]) / 2)
    T.append((L[-1] - R[-1]) / 2)
if L and UD:
    T.append(L[0] - UD[0])
    T.append(L[-1] - UD[-1])
if R and UD:
    T.append(UD[0] - R[0])
    T.append(UD[-1] - R[-1])
if U and D:
    T.append((D[0] - U[0]) / 2)
    T.append((D[-1] - U[-1]) / 2)
if U and LR:
    T.append(-U[0] + LR[0])
    T.append(-U[-1] + LR[-1])
if D and LR:
    T.append(-LR[0] + D[0])
    T.append(-LR[-1] + D[-1])

ans = INF
for t in T:
    if t < 0: continue
    l = INF
    r = -INF
    d = INF
    u = -INF
    if L:
        l = min(l, L[0] - t)
        r = max(r, L[-1] - t)
    if R:
        l = min(l, R[0] + t)
        r = max(r, R[-1] + t)
    if U:
        d = min(d, U[0] + t)
        u = max(u, U[-1] + t)
    if D:
        d = min(d, D[0] - t)
        u = max(u, D[-1] - t)
    if LR:
        d = min(d, LR[0])
        u = max(u, LR[-1])
    if UD:
        l = min(l, UD[0])
        r = max(r, UD[-1])
    ans = min(ans, (r - l) * (u - d))

print(ans)
