(H, W) = map(int, input().split())
s = [list(input()) for _ in range(H)]
jougesayuu = [(-1, 0), (1, 0), (0, -1), (0, 1)]
check = True
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            flag = False
            for (n, m) in jougesayuu:
                (ni, nj) = (i + n, j + m)
                if ni < 0 or H <= ni or nj < 0 or (W <= nj):
                    continue
                if s[ni][nj] == '#':
                    flag = True
            if not flag:
                check = False
print('Yes' if check else 'No')
