INF = float('inf')

N = int(input())

xConstMin, xConstMax = INF, -INF
xAscMin, xAscMax = INF, -INF
xDescMin, xDescMax = INF, -INF
yConstMin, yConstMax = INF, -INF
yAscMin, yAscMax = INF, -INF
yDescMin, yDescMax = INF, -INF
for _ in range(N):
    x, y, d = input().split()
    x, y = int(x), int(y)
    if d == 'R':
        xAscMax = max(xAscMax, x)
        xAscMin = min(xAscMin, x)
        yConstMax = max(yConstMax, y)
        yConstMin = min(yConstMin, y)
    elif d == 'L':
        xDescMax = max(xDescMax, x)
        xDescMin = min(xDescMin, x)
        yConstMax = max(yConstMax, y)
        yConstMin = min(yConstMin, y)
    elif d == 'U':
        xConstMax = max(xConstMax, x)
        xConstMin = min(xConstMin, x)
        yAscMax = max(yAscMax, y)
        yAscMin = min(yAscMin, y)
    elif d == 'D':
        xConstMax = max(xConstMax, x)
        xConstMin = min(xConstMin, x)
        yDescMax = max(yDescMax, y)
        yDescMin = min(yDescMin, y)

tms = []

t1 = max(0, xDescMax - xConstMax)
t2 = max(0, xConstMax - xAscMax)
if t1 >= t2:
    t = max(0, (xDescMax-xAscMax)/2)
    tms.append(t)
else:
    tms.append(t1)
    tms.append(t2)

t1 = max(0, xConstMin - xAscMin)
t2 = max(0, xDescMin - xConstMin)
if t1 >= t2:
    t = max(0, (xDescMin-xAscMin)/2)
    tms.append(t)
else:
    tms.append(t1)
    tms.append(t2)

t1 = max(0, yDescMax - yConstMax)
t2 = max(0, yConstMax - yAscMax)
if t1 >= t2:
    t = max(0, (yDescMax-yAscMax)/2)
    tms.append(t)
else:
    tms.append(t1)
    tms.append(t2)

t1 = max(0, yConstMin - yAscMin)
t2 = max(0, yDescMin - yConstMin)
if t1 >= t2:
    t = max(0, (yDescMin-yAscMin)/2)
    tms.append(t)
else:
    tms.append(t1)
    tms.append(t2)

ans = INF
for tm in tms:
    if tm == INF: continue

    xs = [xConstMin, xConstMax, xAscMin+tm, xAscMax+tm, xDescMin-tm, xDescMax-tm]
    ys = [yConstMin, yConstMax, yAscMin+tm, yAscMax+tm, yDescMin-tm, yDescMax-tm]

    xMin, xMax = INF, -INF
    for x in xs:
        if x == INF or x == -INF: continue
        xMin = min(xMin, x)
        xMax = max(xMax, x)

    yMin, yMax = INF, -INF
    for y in ys:
        if y == INF or y == -INF: continue
        yMin = min(yMin, y)
        yMax = max(yMax, y)

    ans = min(ans, (xMax-xMin)*(yMax-yMin))

print(ans)

