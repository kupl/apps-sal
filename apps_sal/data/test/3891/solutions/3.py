n, m = list(map(int, input().split()))
matrix = []
for i in range(n):
    matrix.append(input())
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "B":
            lu = (i, j)
for i in reversed(list(range(n))):
    for j in reversed(list(range(m))):
        if matrix[i][j] == "B":
            rd = (i, j)
print((lu[0] + rd[0]) // 2 + 1, (lu[1] + rd[1]) // 2 + 1)

