import numpy as np

h, w, *s = open(0).read().split()
h = int(h)
w = int(w)
all = sum(t.count('#') for t in s)

inf = 1 << 30
d = np.full((h + 1, w + 1), inf, dtype=np.int)

d[0][0] = 0
q = [(0, 0)]
for v in q:
    for nv in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ny = v[0] + nv[0]
        nx = v[1] + nv[1]
        if 0 <= nx < w and 0 <= ny < h and d[ny][nx] == inf and s[ny][nx] == '.':
            d[ny][nx] = d[v[0]][v[1]] + 1
            q.append((ny, nx))

if d[h - 1][w - 1] == inf:
    print((-1))
else:
    print((h * w - (d[h - 1][w - 1] + 1) - all))

