n, m = map(int, input().split())
l = [[*map(int, input().split())] for _ in range(n)]
b = [[0] * m for _ in range(n)]
res = []
for i in range(n - 1):
    for j in range(m - 1):
        if all((l[i][j], l[i + 1][j], l[i][j + 1], l[i + 1][j + 1])):
            res.append(f'{i + 1} {j + 1}')
            b[i][j] = b[i + 1][j] = b[i][j + 1] = b[i + 1][j + 1] = 1
if b == l:
    print(len(res))
    print(*res, sep='\n')
else:
    print(-1)
