h, w = list(map(int, input().split()))

ans = 'Yes'


s = []
for i in range(h):
    s += input().split()

# 端の処理を楽にするために周りを . で埋める
# 上端
s.insert(0, ''.join(['.'] * (w + 2)))
# 両端
s = list(map(lambda x: '.' + x + '.', s))
# 下端
s.insert(len(s), ''.join(['.'] * (w + 2)))

# 1文字ずつリストにする
s = list(map(list, s))

# 50 * 50
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == '#':
            # 上下左右をチェック
            # 仲間がいる時False、孤立しているときTrue
            flg_up = False if s[i - 1][j] == '#' else True
            flg_down = False if s[i + 1][j] == '#' else True
            flg_left = False if s[i][j - 1] == '#' else True
            flg_right = False if s[i][j + 1] == '#' else True

            # 1つでも孤立でないフラグがあれば孤立でないのでFalse、全部孤立の時True
            if flg_up & flg_down & flg_left & flg_right:
                ans = 'No'
                break
    else:
        continue
    break

print(ans)
