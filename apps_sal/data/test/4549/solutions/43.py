(h, w) = list(map(int, input().split()))
ans = 'Yes'
s = []
for i in range(h):
    s += input().split()
s = list(map(list, s))
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if i > 0:
                flg_up = False if s[i - 1][j] == '#' else True
            else:
                flg_up = True
            if i < h - 1:
                flg_down = False if s[i + 1][j] == '#' else True
            else:
                flg_down = True
            if j > 0:
                flg_left = False if s[i][j - 1] == '#' else True
            else:
                flg_left = True
            if j < w - 1:
                flg_right = False if s[i][j + 1] == '#' else True
            else:
                flg_right = True
            if flg_up & flg_down & flg_left & flg_right:
                ans = 'No'
                break
    else:
        continue
    break
print(ans)
