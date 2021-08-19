import copy
(h, w) = map(int, input().split())
s = [input() for _ in range(h)]
a = []
for i in range(-1, 2):
    for j in range(-1, 2):
        a.append((i, j))
ans = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            ans[i][j] = '#'
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            cnt = 0
            for (y, x) in a:
                (iy, jx) = (i + y, j + x)
                if 0 <= iy < h and 0 <= jx < w:
                    if s[iy][jx] == '#':
                        cnt += 1
            ans[i][j] = cnt
for i in ans:
    print(''.join(map(str, i)))
