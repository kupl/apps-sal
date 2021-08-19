(a, b) = list(map(int, input().split()))
s = input()
p = [[0, 0]]
d = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
for c in s:
    p.append([p[-1][0] + d[c][0], p[-1][1] + d[c][1]])
(px, py) = (p[-1][0], p[-1][1])
for (x, y) in p:
    k = 0
    if px:
        k = (a - x) // px
    elif py:
        k = (b - y) // py
    if k >= 0 and x + k * px == a and (y + k * py == b):
        print('Yes')
        break
else:
    print('No')
