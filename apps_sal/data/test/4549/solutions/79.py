h, w = list(map(int, input().split()))

ans = 'Yes'

s = []
for i in range(h):
    s += input().split()

# 端の処理を楽にするために周りを . で埋める
#   ..........
#   .#.#.#.#..
#   ..##.###..
#   .....##.#.
#   ...##...#.
#   ..####..#.
#   ..........

## 上端
s.insert(0, ''.join(['.'] * (w + 2)))
## 両端
s = list(map(lambda x: '.' + x + '.', s))
## 下端
s.insert(len(s), ''.join(['.'] * (w + 2)))

# 1文字ずつリストにする
s = list(map(list, s))

# 50 * 50
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if (s[i][j] == '#') & (s[i-1][j] == '.') & (s[i+1][j] == '.') & (s[i][j-1] == '.') & (s[i][j+1] == '.'):
            ans = 'No'
            break
    else:
        continue
    break

print(ans)
