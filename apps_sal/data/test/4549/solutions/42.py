h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

for i in range(h):
    s[i].insert(0, '.')
    s[i].append('.')

s.insert(0, ['.'] * (w + 2))
s.append(['.'] * (w + 2))

flag = True
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == '
            if s[i - 1][j] == '
                    or s[i + 1][j] == '
                    or s[i][j - 1] == '
                    or s[i][j + 1] == '
                continue
            else:
                flag = False
                break
    if flag == False:
        print('No')
        break
else:
    print('Yes')
