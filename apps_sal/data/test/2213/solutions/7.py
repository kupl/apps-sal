n, m, k = list(map(int, input().split()))
for i in range(n):
    a = list(map(int, input().split()))
if k == 0:
    x = 1
    y = m + 1
    z = 1
else:
    x = m
    y = 0
    z = -1
print(m * (m - 1) // 2)
for i in range(x, y, z):
    for j in range(x, y, z):
        if k == 0 and i < j:
            print(i, j)
        if k == 1 and i > j:
            print(i, j)

