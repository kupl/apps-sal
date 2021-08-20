(H, W) = map(int, input().split())
S = [list(input()) for _ in range(H)]
ans = [[0 for _ in range(W)] for _ in range(H)]
move = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            ans[i][j] = '#'
        else:
            for (x, y) in move:
                (nx, ny) = (i + x, j + y)
                if nx < 0 or H <= nx or ny < 0 or (W <= ny):
                    continue
                elif S[nx][ny] == '#':
                    ans[i][j] += 1
for a in ans:
    for i in range(W):
        a[i] = str(a[i])
    print(''.join(a))
