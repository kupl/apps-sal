(n, m) = [int(el) for el in input().split()]
col = 2
a = [int(el) for el in input().split()]
for i in range(n - 1):
    if a[i + 1] - a[i] == m * 2:
        col += 1
    if a[i + 1] - a[i] > m * 2:
        col += 2
print(col)
