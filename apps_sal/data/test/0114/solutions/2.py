(n, m) = list(map(int, input().split()))
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
    x = A[-1].count(1)
res = []
marked = [[0] * m for _ in range(n)]
for i in range(n - 1):
    for j in range(m - 1):
        if A[i][j] == 1:
            if A[i + 1][j] == 1 and A[i][j + 1] == 1 and (A[i + 1][j + 1] == 1):
                marked[i][j] = 1
                marked[i + 1][j] = 1
                marked[i + 1][j + 1] = 1
                marked[i][j + 1] = 1
                res.append((i + 1, j + 1))
if marked == A:
    print(len(res))
    for item in res:
        print(item[0], item[1])
else:
    print(-1)
