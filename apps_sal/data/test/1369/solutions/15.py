import itertools
import math
n = int(input())
l = [[0, 0] for _ in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    l[i][0] = x
    l[i][1] = y

if n == 2:
    r = math.sqrt((l[1][0] - l[0][0])**2 + (l[1][1] - l[0][1])**2) / 2
    print(r)
    return

ans = float('inf')
combs = list(itertools.combinations(range(n), 3))
for comb in combs:
    x0, y0 = l[comb[0]]
    x1, y1 = l[comb[1]]
    x2, y2 = l[comb[2]]

    a = x1 - x0
    b = y1 - y0
    p = (x1**2 - x0**2 + y1**2 - y0**2) / 2

    c = x2 - x0
    d = y2 - y0
    q = (x2**2 - x0**2 + y2**2 - y0**2) / 2

    if a * d - b * c == 0:
        continue
    xc = (p * d - q * b) / (a * d - b * c)
    yc = (-p * c + q * a) / (a * d - b * c)
    r = math.sqrt((x0 - xc)**2 + (y0 - yc)**2)
    for i in range(n):
        x, y = l[i]
        if math.sqrt((x - xc)**2 + (y - yc)**2) > r:
            break
    else:
        ans = min(ans, r)

combs = list(itertools.combinations(range(n), 2))
for comb in combs:
    x0, y0 = l[comb[0]]
    x1, y1 = l[comb[1]]
    xc = (x0 + x1) / 2
    yc = (y0 + y1) / 2
    r = math.sqrt((x0 - xc)**2 + (y0 - yc)**2)
    for i in range(n):
        x, y = l[i]
        if math.sqrt((x - xc)**2 + (y - yc)**2) > r:
            break
    else:
        ans = min(ans, r)
print(ans)
