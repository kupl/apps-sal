(n, m) = map(int, input().split())
matrix = [[] for i in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))
flag = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            if i == 0 or i == n - 1 or j == 0 or (j == m - 1):
                flag = 1
if flag == 0:
    print(4)
else:
    print(2)
