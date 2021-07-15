n, k = map(int, input().split())
t = list(map(int, input().split()))
p = [0] * 1001
x = y = d = 0
for h in t:
    s = h - d
    if s > 0:
        p[s] += 1
        if p[s] > x: x, y = p[s], s
    d += k
d = 0
for i, h in enumerate(t):
    t[i] = y - h + d
    d += k
t = ['- ' + str(i) + ' ' + str(-s) if s < 0 else '+ ' + str(i) + ' ' + str(s) for i, s in enumerate(t, 1) if s]
print(n - x)
print('\n'.join(t))
