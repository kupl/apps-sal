s = 10 * [0]
for i in range(10):
    s[i] = input()


def trav(i, j, s, n):
    if n == 1:
        if(i < 9):
            if s[i + 1][j] == 'X':
                return 1 + trav(i + 1, j, s, n)
            return 0
        return 0
    if n == -1:
        if(i > 0):
            if s[i - 1][j] == 'X':
                return 1 + trav(i - 1, j, s, n)
            return 0
        return 0
    if n == 2:
        if(j < 9):
            if s[i][j + 1] == 'X':
                return 1 + trav(i, j + 1, s, n)
            return 0
        return 0
    if n == -2:
        if(j > 0):
            if s[i][j - 1] == 'X':
                return 1 + trav(i, j - 1, s, n)
            return 0
        return 0
    if n == 3:
        if(i < 9 and j < 9):
            if s[i + 1][j + 1] == 'X':
                return 1 + trav(i + 1, j + 1, s, n)
            return 0
        return 0
    if n == -3:
        if(i > 0 and j > 0):
            if s[i - 1][j - 1] == 'X':
                return 1 + trav(i - 1, j - 1, s, n)
            return 0
        return 0
    if n == 4:
        if(i > 0 and j < 9):
            if s[i - 1][j + 1] == 'X':
                return 1 + trav(i - 1, j + 1, s, n)
            return 0
        return 0
    if n == -4:
        if(i < 9 and j > 0):
            if s[i + 1][j - 1] == 'X':
                return 1 + trav(i + 1, j - 1, s, n)
            return 0
        return 0


flag = False
for i in range(10):
    for j in range(10):
        if s[i][j] == '.':
            # print(trav(i,j,s,-2))
            # input()
            if trav(i, j, s, 1) + trav(i, j, s, -1) >= 4 or trav(i, j, s, 2) + trav(i, j, s, -2) >= 4 or trav(i, j, s, 3) + trav(i, j, s, -3) >= 4 or trav(i, j, s, 4) + trav(i, j, s, -4) >= 4:
                flag = True;
                print('YES')
                break
    if flag:
        break
if not flag:
    print('NO')
