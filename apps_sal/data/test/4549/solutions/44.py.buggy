h, w = map(int, input().split())
s = [input() for i in range(h)]
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if s[i][j] == '#':
            if (s[i + 1][j] == '#' or s[i - 1][j] == '#' or s[i][j + 1] == '#' or s[i][j - 1] == '#'):
                continue
            else:
                print('No')
                return
print('Yes')
