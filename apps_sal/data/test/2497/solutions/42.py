N = int(input())
 
PS = [[], [], [], []]
S = "RLUD".index
 
for i in range(N):
    x, y, d = input().split(); x = int(x); y = int(y)
    PS[S(d)].append((x, y))
 
T = [0]
INF = 10**9
 
dymin = INF; dymax = -INF
P = []
for i in [0, 1]:
    xmin = INF; xmax = -INF
    for x, y in PS[i]:
        dymin = min(dymin, y)
        dymax = max(dymax, y)
        xmin = min(xmin, x)
        xmax = max(xmax, x)
    P.append((xmin, xmax))
for x0 in P[0]:
    for x1 in P[1]:
        T.append(max(x1 - x0, 0) / 2.)
 
dxmin = INF; dxmax = -INF
Q = []
for i in [2, 3]:
    ymin = INF; ymax = -INF
    for x, y in PS[i]:
        dxmin = min(dxmin, x)
        dxmax = max(dxmax, x)
        ymin = min(ymin, y)
        ymax = max(ymax, y)
    Q.append((ymin, ymax))
for y0 in Q[0]:
    for y1 in Q[1]:
        T.append(max(y1 - y0, 0) / 2.)
 
for x0 in [dxmin, dxmax]:
    for x in P[0]:
        T.append(max(x0 - x, 0))
    for x in P[1]:
        T.append(max(x - x0, 0))
for y0 in [dymin, dymax]:
    for y in Q[0]:
        T.append(max(y0 - y, 0))
    for y in Q[1]:
        T.append(max(y - y0, 0))
 
ans = 10**30
for t in T:
    xmin = dxmin; xmax = dxmax
    ymin = dymin; ymax = dymax
 
    xi, xa = P[0]
    if xi != INF:
        xmin = min(xmin, xi+t)
        xmax = max(xmax, xa+t)
    xi, xa = P[1]
    if xi != INF:
        xmin = min(xmin, xi-t)
        xmax = max(xmax, xa-t)
    yi, ya = Q[0]
    if yi != INF:
        ymin = min(ymin, yi+t)
        ymax = max(ymax, ya+t)
    yi, ya = Q[1]
    if yi != INF:
        ymin = min(ymin, yi-t)
        ymax = max(ymax, ya-t)
    ans = min(ans, (xmax - xmin) * (ymax - ymin))
print("%.6f" % ans)
