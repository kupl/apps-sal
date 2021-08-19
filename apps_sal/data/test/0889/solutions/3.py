s = []
suc = 0
for i in range(4):
    s.append(input())
for i in range(3):
    for j in range(3):
        if s[i][j].count('#') + s[i + 1][j].count('#') + s[i][j + 1].count('#') + s[i + 1][j + 1].count('#') != 2:
            suc = 1
if suc == 1:
    print('YES')
else:
    print('NO')
