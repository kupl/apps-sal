H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
# 列について
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            break
    # すべて空白だったらx印
    else:
        for l in range(W):
            A[i][l] = "x"

# 行について
for i in range(W):
    for j in range(H):
        if A[j][i] == "#":
            break
    else:
        for l in range(H):
            A[l][i] = "x"
for i in range(H):
    x_cnt = 0
    for j in range(W):
        if A[i][j] != "x":
            print(A[i][j], end="")
        else:
            x_cnt += 1

    if x_cnt < W:
        print()
    else:
        pass
