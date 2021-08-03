n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
col = [[0, 0] for i in range(m)]
row = [[0, 0] for i in range(n)]
for i in range(n):
    summa = sum(a[i])
    row[i] = [summa, m - summa]

for i in range(m):
    summa = 0
    for j in range(n):
        summa += a[j][i]
    col[i] = [summa, n - summa]

res = 0
for i in row:
    res += (2 ** i[0]) + (2 ** i[1]) - 2

for i in col:
    res += (2 ** i[0]) + (2 ** i[1]) - 2

res -= n * m
print(res)
