import copy

h, w = list(map(int, input().split()))
s = [list(input()) for _ in range(h)]

dir = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
ans = copy.deepcopy(s)
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            cnt = 0
            for y, x in dir:
                iy, jx = i+y, j+x
                if 0 <= iy < h and 0 <= jx < w:
                    if s[iy][jx] == '#':
                        cnt += 1
            ans[i][j] = cnt
for i in ans:
    print((''.join(map(str, i))))

