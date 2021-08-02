n = int(input())
a = [[1 if row == 0 or col == 0 else 0 for col in range(n)] for row in range(n)]
for row in range(1, n):
    for col in range(1, n):
        a[row][col] = a[row - 1][col] + a[row][col - 1]
print(max(max(a)))
