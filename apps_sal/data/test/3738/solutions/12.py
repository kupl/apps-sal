R = lambda: map(int, input().split())
a, b = R()
cs = [[0, 0]]
d = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
for c in input():
    cs.append([cs[-1][0] + d[c][0], cs[-1][1] + d[c][1]])
px, py = cs[-1][0], cs[-1][1]
for x, y in cs:
    k = 0
    if px:
        k = (a - x) // px
    elif py:
        k = (b - y) // py
    if k >= 0 and x + k * px == a and y + k * py == b:
        print('Yes')
        return
print('No')
