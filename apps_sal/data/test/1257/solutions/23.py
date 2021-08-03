n, k = map(int, input().strip().split())

a = [[0 for x in range(n)] for x in range(n)]
cur = n * n
for i in range(0, n):
    for j in range(n - 1, k - 2, -1):
        a[i][j] = cur
        cur -= 1

for i in range(0, n):
    for j in range(k - 2, -1, -1):
        a[i][j] = cur
        cur -= 1

total = 0
for i in range(0, n):
    total += a[i][k - 1]

print(total)
for i in range(0, n):
    for j in range(0, n):
        print(a[i][j], end=" ")
    print()
