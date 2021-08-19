def mine_count(x, y, ans):
    ans[y][x] = 0
    for (nx, ny) in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
        if 0 <= y + ny < H and 0 <= x + nx < W:
            if ans[y + ny][x + nx] == '#':
                ans[y][x] += 1
    return ans


(H, W) = map(int, input().split())
S = [list(input()) for _ in range(H)]
ans = S
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            ans = mine_count(j, i, ans)
for row in ans:
    for item in row:
        print(item, end='')
    print()
