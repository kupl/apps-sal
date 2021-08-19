from itertools import product
(H, W) = list(map(int, input().split()))
s = [input() for _ in range(H)]
for (i, j) in product(list(range(H)), list(range(W))):
    if s[i][j] == '.':
        continue
    is_ok = False
    for (di, dj) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        (ni, nj) = (i + di, j + dj)
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if s[ni][nj] == '#':
            is_ok = True
    if not is_ok:
        print('No')
        break
else:
    print('Yes')
