(H, W) = [int(x) for x in input().split()]
pic = [list(input()) for _ in range(H)]
ans = [['#' for i in range(W + 2)] for j in range(H + 2)]
for i in range(H):
    for j in range(W):
        ans[i + 1][j + 1] = pic[i][j]
low = ''
for i in range(H + 2):
    for j in range(W + 2):
        low += ans[i][j]
    print(low)
    low = ''
