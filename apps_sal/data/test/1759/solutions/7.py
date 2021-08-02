m, n = map(int, input().split())
t = []
for i in range(m):
    t += [list(map(int, input().split()))]
d = [0] * m
for i in range(n):
    d[0] += t[0][i]
    for j in range(1, m):
        d[j] = max(d[j - 1], d[j]) + t[j][i]
print(*d)
