s = [[] for i in range(4)]
s[0] = [i for i in input()]
s[1] = [i for i in input()]
s[2] = [i for i in input()]
s[3] = [i for i in input()]
a = 0
for i in range(4):
    for j in range(4):
        if i > 1:
            if s[i][j] == '.' and s[i - 1][j] == 'x' and (s[i - 2][j] == 'x'):
                print('YES')
                a = 1
                break
            if j > 1:
                if s[i][j] == '.' and s[i - 1][j - 1] == 'x' and (s[i - 2][j - 2] == 'x'):
                    print('YES')
                    a = 1
                    break
            if j < 2:
                if s[i][j] == '.' and s[i - 1][j + 1] == 'x' and (s[i - 2][j + 2] == 'x'):
                    print('YES')
                    a = 1
                    break
        if i < 2:
            if s[i][j] == '.' and s[i + 1][j] == 'x' and (s[i + 2][j] == 'x'):
                print('YES')
                a = 1
                break
            if j > 1:
                if s[i][j] == '.' and s[i + 1][j - 1] == 'x' and (s[i + 2][j - 2] == 'x'):
                    print('YES')
                    a = 1
                    break
            if j < 2:
                if s[i][j] == '.' and s[i + 1][j + 1] == 'x' and (s[i + 2][j + 2] == 'x'):
                    print('YES')
                    a = 1
                    break
        if j > 1:
            if s[i][j] == '.' and s[i][j - 1] == 'x' and (s[i][j - 2] == 'x'):
                print('YES')
                a = 1
                break
        if j < 2:
            if s[i][j] == '.' and s[i][j + 1] == 'x' and (s[i][j + 2] == 'x'):
                print('YES')
                a = 1
                break
        if i != 3 and i != 0:
            if s[i][j] == '.' and s[i + 1][j] == 'x' and (s[i - 1][j] == 'x'):
                print('YES')
                a = 1
                break
            if j != 3 and j != 0:
                if s[i][j] == '.' and s[i + 1][j + 1] == 'x' and (s[i - 1][j - 1] == 'x'):
                    print('YES')
                    a = 1
                    break
                if s[i][j] == '.' and s[i - 1][j + 1] == 'x' and (s[i + 1][j - 1] == 'x'):
                    print('YES')
                    a = 1
                    break
        if j != 3 and j != 0:
            if s[i][j] == '.' and s[i][j + 1] == 'x' and (s[i][j - 1] == 'x'):
                print('YES')
                a = 1
                break
    if a:
        break
else:
    print('NO')
