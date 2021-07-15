x, y, m = map(int, input().split())
if max(x, y) >= m:
    print(0)
elif max(x, y) <= 0:
    print(-1)
else:
    p, val = sorted([x, y]), 0
    if p[0] < 0:
        s = (min(m, 0) - p[0]) // p[1]
        p[0] += s * p[1]
        val += s
    while max(p) < m:
        p, val = [sum(p), max(p)], val + 1
    print(val)
