n, m = list(map(int, input().split()))
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

ans = [[0 for i in range(m)] for j in range(n)]
anslist = []
for i in range(n - 1):
    for j in range(m - 1):
        if mat[i][j] == 1 and mat[i][j + 1] == 1 and mat[i + 1][j] == 1 and mat[i + 1][j + 1]:
            for k in range(2):
                for l in range(2):
                    ans[i + k][j + l] = 1
            anslist.append([i + 1, j + 1])


if mat == ans:
    print(len(anslist))
    for i, j in anslist:
        print(i, j)
else:
    print(-1)
