n, m = list(map(int, input().split()))
li = [list(map(int, input().split())) for _ in range(n)]
b = [[0 for _ in range(m)] for _ in range(n)]
res = []
for i in range(n - 1):
    for j in range(m - 1):
        if li[i][j] == li[i + 1][j] == li[i][j + 1] == li[i + 1][j + 1] == 1:
            res.append([i + 1, j + 1])
            b[i][j] = 1
            b[i + 1][j] = 1
            b[i + 1][j + 1] = 1
            b[i][j + 1] = 1
if li == b:
    print(len(res))
    for i in res:
        print(*i)
else:
    print(-1)
