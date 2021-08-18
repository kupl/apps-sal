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
        flg_up = True if s[i - 1][j] == '.' else False
        flg_down = True if s[i + 1][j] == '.' else False
        flg_left = True if s[i][j - 1] == '.' else False
        flg_right = True if s[i][j + 1] == '.' else False

        if (s[i - 1][j] == '.') & (s[i + 1][j] == '.') & (s[i][j - 1] == '.') & (s[i][j + 1] == '.'):
            ans = 'No'
            break
    else:
        continue
    break

print(ans)
