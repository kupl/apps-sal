H, W = map(int, input().split())

S = [input() for _ in range(H)]
M = [[""] * W for _ in range(H)]


def bomb_cnt(i, j):
    min_h = max(0, i - 1)
    max_h = min(i + 2, H)
    min_w = max(0, j - 1)
    max_w = min(j + 2, W)
    cnt = 0
    for k in range(min_h, max_h):
        for g in range(min_w, max_w):
            if (S[k][g] == "#"):
                cnt += 1

    return str(cnt)


for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            M[i][j] = "#"
        else:
            M[i][j] = bomb_cnt(i, j)


for i in range(H):
    print(*M[i], sep="")
