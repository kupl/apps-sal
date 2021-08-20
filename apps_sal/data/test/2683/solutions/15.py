def prt(temp):
    for i in temp:
        print(i)


def isin(x, a, b):
    return a <= x and x <= b


def prog():
    (n, k) = list(map(int, input().split()))
    mat = []
    dots = []
    for i in range(n):
        inp = input()
        temp = []
        for x1 in range(n):
            x = inp[x1]
            if x == 'X':
                temp += [1]
            else:
                temp += [0]
            if x == '.':
                dots += [(i, x1)]
        mat += [temp]
    if len(dots) == 0:
        return False
    mat[dots[0][0]][dots[0][1]] = 1
    if prog1(mat, n, k):
        return True
    for i in range(1, len(dots)):
        mat[dots[i - 1][0]][dots[i - 1][1]] = 0
        mat[dots[i][0]][dots[i][1]] = 1
        if prog1(mat, n, k):
            return True
    if prog1(mat, n, k):
        return True
    return False


def prog1(mat, n, k):
    temp = []
    temp1 = []
    for i in mat:
        temp += [i[:]]
        temp1 += [i[:]]
    for i in range(n):
        j = 0
        for j in range(1, k):
            temp[i][j] += temp[i][j - 1]
        if temp[i][j] == k:
            return True
        for j in range(k, n):
            temp[i][j] += temp[i][j - 1]
            if temp[i][j] - temp[i][j - k] == k:
                return True
    for i in range(n):
        for j in range(n):
            temp[i][j] = temp1[j][i]
    for i in range(n):
        j = 0
        for j in range(1, k):
            temp[i][j] += temp[i][j - 1]
        if temp[i][j] == k:
            return True
        for j in range(k, n):
            temp[i][j] += temp[i][j - 1]
            if temp[i][j] - temp[i][j - k] == k:
                return True
    for i in range(n):
        for j in range(n):
            temp[i][j] = temp1[i][j]
    for i in range(n - 1, -1, -1):
        x = i
        y = 0
        cn = 1
        while cn != k and isin(y + 1, 0, n - 1) and isin(x + 1, 0, n - 1):
            x += 1
            y += 1
            temp[x][y] += temp[x - 1][y - 1]
            cn += 1
        if temp[x][y] == k:
            return True
        while cn >= k and isin(y + 1, 0, n - 1) and isin(x + 1, 0, n - 1):
            x += 1
            y += 1
            temp[x][y] += temp[x - 1][y - 1]
            if temp[x][y] - temp[x - k][y - k] == k:
                return True
    for i in range(1, n):
        x = 0
        y = i
        cn = 1
        while cn != k and isin(y + 1, 0, n - 1) and isin(x + 1, 0, n - 1):
            x += 1
            y += 1
            temp[x][y] += temp[x - 1][y - 1]
            cn += 1
        if temp[x][y] == k:
            return True
        while cn >= k and isin(y + 1, 0, n - 1) and isin(x + 1, 0, n - 1):
            x += 1
            y += 1
            temp[x][y] += temp[x - 1][y - 1]
            if temp[x][y] - temp[x - k][y - k] == k:
                return True
    for i in range(n):
        for j in range(n):
            temp[i][j] = temp1[i][n - 1 - j]
    for i in range(n - 1, -1, -1):
        x = i
        y = 0
        cn = 1
        while cn != k and isin(y + 1, 0, n - 1) and isin(x + 1, 0, n - 1):
            x += 1
            y += 1
            temp[x][y] += temp[x - 1][y - 1]
            cn += 1
        if temp[x][y] == k:
            return True
        while cn >= k and isin(y + 1, 0, n - 1) and isin(x + 1, 0, n - 1):
            x += 1
            y += 1
            temp[x][y] += temp[x - 1][y - 1]
            if temp[x][y] - temp[x - k][y - k] == k:
                return True
    for i in range(1, n):
        x = 0
        y = i
        cn = 1
        while cn != k and isin(y + 1, 0, n - 1) and isin(x + 1, 0, n - 1):
            x += 1
            y += 1
            temp[x][y] += temp[x - 1][y - 1]
            cn += 1
        if temp[x][y] == k:
            return True
        while cn >= k and isin(y + 1, 0, n - 1) and isin(x + 1, 0, n - 1):
            x += 1
            y += 1
            temp[x][y] += temp[x - 1][y - 1]
            if temp[x][y] - temp[x - k][y - k] == k:
                return True
    return False


t = eval(input())
for _ in range(t):
    ans = prog()
    if ans == True:
        print('YES')
    else:
        print('NO')
