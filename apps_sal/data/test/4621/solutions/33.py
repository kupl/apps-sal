(H, W) = map(int, input().split())
C = [input() for i in range(H)]
ans = ['' for i in range(H * 2)]
for i in range(H):
    for j in range(W):
        ans[2 * i] += C[i][j]
        ans[2 * i + 1] += C[i][j]
for i in range(2 * H):
    print(ans[i])
