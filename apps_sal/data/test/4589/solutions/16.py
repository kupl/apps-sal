(h, w) = map(int, input().split())
s = []
for _ in range(h):
    s.append(list(input()))
if (h == 1) & (w == 1):
    if s[0][0] == '.':
        s[0][0] = '0'
elif (h == 1) & (w != 1):
    for j in range(w):
        if j == 0:
            s[0][j] = s[0][j].replace('.', str(s[0][j + 1].count('#')))
        elif j == w - 1:
            s[0][j] = s[0][j].replace('.', str(s[0][j - 1].count('#')))
        else:
            s[0][j] = s[0][j].replace('.', str([s[0][j - 1], s[0][j + 1]].count('#')))
elif (h != 1) & (w == 1):
    for i in range(h):
        if i == 0:
            s[i][0] = s[i][0].replace('.', str(s[i + 1][0].count('#')))
        elif i == h - 1:
            s[i][0] = s[i][0].replace('.', str(s[i - 1][0].count('#')))
        else:
            s[i][0] = s[i][0].replace('.', str([s[i - 1][0], s[i + 1][0]].count('#')))
else:
    for i in range(len(s)):
        if i == 0:
            for j in range(w):
                if j == 0:
                    s[i][j] = s[i][j].replace('.', str([s[i][j + 1], s[i + 1][j], s[i + 1][j + 1]].count('#')))
                elif j == w - 1:
                    s[i][j] = s[i][j].replace('.', str([s[i][j - 1], s[i + 1][j], s[i + 1][j - 1]].count('#')))
                else:
                    s[i][j] = s[i][j].replace('.', str([s[i][j - 1], s[i][j + 1], s[i + 1][j], s[i + 1][j + 1], s[i + 1][j - 1]].count('#')))
        elif i == h - 1:
            for j in range(w):
                if j == 0:
                    s[i][j] = s[i][j].replace('.', str([s[i][j + 1], s[i - 1][j], s[i - 1][j + 1]].count('#')))
                elif j == w - 1:
                    s[i][j] = s[i][j].replace('.', str([s[i][j - 1], s[i - 1][j], s[i - 1][j - 1]].count('#')))
                else:
                    s[i][j] = s[i][j].replace('.', str([s[i][j - 1], s[i][j + 1], s[i - 1][j], s[i - 1][j + 1], s[i - 1][j - 1]].count('#')))
        else:
            for j in range(w):
                if j == 0:
                    s[i][j] = s[i][j].replace('.', str([s[i][j + 1], s[i - 1][j], s[i - 1][j + 1], s[i + 1][j], s[i + 1][j + 1]].count('#')))
                elif j == w - 1:
                    s[i][j] = s[i][j].replace('.', str([s[i][j - 1], s[i - 1][j], s[i - 1][j - 1], s[i + 1][j], s[i + 1][j - 1]].count('#')))
                else:
                    s[i][j] = s[i][j].replace('.', str([s[i][j - 1], s[i][j + 1], s[i - 1][j], s[i - 1][j + 1], s[i - 1][j - 1], s[i + 1][j], s[i + 1][j + 1], s[i + 1][j - 1]].count('#')))
for k in s:
    print(''.join(k))
