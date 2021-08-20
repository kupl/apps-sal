(m, n) = map(int, input().split())
t = [[0] * (n + 1)]
for i in range(m):
    t.append([0] + list(map(int, input().split())))
fin = []
for i in range(n + 1):
    fin.append([0] * (m + 1))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        fin[i][j] = max(fin[i][j - 1], fin[i - 1][j]) + t[j][i]
print(' '.join(map(str, fin[n][1:])))
