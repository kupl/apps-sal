h, w = list(map(int, input().split()))

ans = 'Yes'


s = []
for i in range(h):
    s += input().split()

s.insert(0, ''.join(['.'] * (w + 2)))
s = list(map(lambda x: '.' + x + '.', s))
s.insert(len(s), ''.join(['.'] * (w + 2)))

s = list(map(list, s))

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == '
        flg_up = False if s[i - 1][j] == '
        flg_down = False if s[i + 1][j] == '
        flg_left = False if s[i][j - 1] == '
        flg_right = False if s[i][j + 1] == '

        if flg_up & flg_down & flg_left & flg_right:
            ans = 'No'
            break
    else:
        continue
    break

print(ans)
