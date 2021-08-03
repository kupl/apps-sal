n, m = map(int, input().split())
t = [list(map(int, input().split())) for i in range(n)]
for j in range(m - 1):
    t[0][j + 1] += t[0][j]
for i in range(n - 1):
    t[i + 1][0] += t[i][0]
    for j in range(m - 1):
        t[i + 1][j + 1] += max(t[i + 1][j], t[i][j + 1])
print(' '.join(map(str, [p[m - 1] for p in t])))
