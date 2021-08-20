import sys
n = int(input())
inf = float('inf')
xmin = [inf, inf, inf]
xmax = [-inf, -inf, -inf]
ymin = [inf, inf, inf]
ymax = [-inf, -inf, -inf]
for _ in range(n):
    (x, y, d) = [i for i in input().split()]
    x = int(x)
    y = int(y)
    if d == 'U':
        ud = 2
        lr = 1
    if d == 'D':
        ud = 0
        lr = 1
    if d == 'L':
        ud = 1
        lr = 0
    if d == 'R':
        ud = 1
        lr = 2
    xmin[lr] = min(xmin[lr], x)
    xmax[lr] = max(xmax[lr], x)
    ymin[ud] = min(ymin[ud], y)
    ymax[ud] = max(ymax[ud], y)


def lpos(t):
    return min([(v - 1) * t + i for (v, i) in enumerate(xmin)])


def rpos(t):
    return max([(v - 1) * t + i for (v, i) in enumerate(xmax)])


def dpos(t):
    return min([(v - 1) * t + i for (v, i) in enumerate(ymin)])


def upos(t):
    return max([(v - 1) * t + i for (v, i) in enumerate(ymax)])


s = {0}
for i in range(3):
    for j in range(i + 1, 3):
        t = (xmin[j] - xmin[i]) / (i - j)
        if t > 0 and t != inf and (t != -inf):
            s.add(t)
        t = (xmax[j] - xmax[i]) / (i - j)
        if 0 < t and t != inf and (t != -inf):
            s.add(t)
        t = (ymin[j] - ymin[i]) / (i - j)
        if 0 < t and t != inf and (t != -inf):
            s.add(t)
        t = (ymax[j] - ymax[i]) / (i - j)
        if 0 < t and t != inf and (t != -inf):
            s.add(t)
ans = 10 ** 18
for t in s:
    area = (rpos(t) - lpos(t)) * (upos(t) - dpos(t))
    if area < ans:
        ans = area
print(ans)
