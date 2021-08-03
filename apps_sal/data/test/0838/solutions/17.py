n, m = list(map(int, input().split()))

mtx = []
for _ in range(n):
    mtx.append(list(map(int, input().split())))

res = 0
for i in range(n):
    a = sum(mtx[i])
    b = m - a
    if a >= 1:
        res += 2 ** a - 1
    if b >= 1:
        res += 2 ** b - 1

for j in range(m):
    a = sum(mtx[i][j] for i in range(n))
    b = n - a
    if a >= 1:
        res += 2 ** a - 1
    if b >= 1:
        res += 2 ** b - 1

res -= n * m
print(res)
