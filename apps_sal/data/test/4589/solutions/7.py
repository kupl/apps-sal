H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

di = [1, 1, 0, -1, -1, -1, 0, 1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(H):
    for j in range(W):
        ans = 0
        if S[i][j] == '#':
            continue
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or nj < 0 or ni >= H or nj >= W:
                continue
            if S[ni][nj] == '#':
                ans += 1
        S[i][j] = str(ans)
for i in range(H):
    for j in range(W):
        print(S[i][j], end='')
    print()
