H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = [[0] * W for _ in range(H)]
x = (-1, 0, 1, -1, 0, 1, -1, 0, 1)
y = (1, 1, 1, 0, 0, 0, -1, -1, -1)
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            for k in range(9):
                a = i + y[k]
                b = j + x[k]
                if 0 <= a < H and 0 <= b < W:
                    if S[a][b] == "#":
                        ans[i][j] += 1
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            print("#", end="")
        else:
            print(ans[i][j], end="")
    print()
