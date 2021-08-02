n, m, k = map(int, input().split())
p, s, t = [[] for y in range(m)], [0] * n, [0] * m
for x in range(n):
    for y, c in enumerate(input()[:: 2]):
        if c == '1':
            p[y].append(x)
for i in range(k):
    x, y = map(int, input().split())
    s[x - 1] -= 1
    t[y - 1] += 1
for y, d in enumerate(t):
    for x in p[y]:
        s[x] += d
print(' '.join(map(str, s)))
