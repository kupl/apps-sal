n, c = map(int, input().split())
lis = [list(map(int, input().split())) for i in range(c)]
li = [list(map(int, input().split())) for i in range(n)]
ans = 10 ** 100
cnt = [0, 0, 0]
masu = [[0 for i in range(c)] for j in range(3)]
for i in range(n):
    for j in range(n):
        cnt[(i + j) % 3] += 1
        masu[(i + j) % 3][li[i][j] - 1] += 1
for i in range(c):
    for j in range(c):
        if i != j:
            for k in range(c):
                if i != k and j != k:
                    tryans = 0
                    num = [i, j, k]
                    for l in range(3):
                        for h in range(c):
                            if h != num[l]:
                                tryans += lis[h][num[l]] * masu[l][h]
                    ans = min(ans, tryans)
print(ans)
