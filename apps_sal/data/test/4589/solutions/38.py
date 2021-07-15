H, W = map(int, input().split())
S = [[a for a in input()] for _ in range(H)]
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#": continue
        c = 0
        for ii, jj in d:
            ni = i + ii
            nj = j + jj
            if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == "#":
                c += 1
        S[i][j] = str(c)
for s in S:
    print("".join(s))
