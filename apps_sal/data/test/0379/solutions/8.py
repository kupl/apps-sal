n, m = list(map(int, input().split()))
s = []
for i in range(n):
    s += [input()]


def check():
    flag = False
    for i in range(n):
        for j in range(m):
            if s[i][j] == 'X':
                i1 = i
                j1 = j
                flag = True
                break
        if flag: break

    flag = False
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if s[i][j] == 'X':
                i2 = i
                j2 = j
                flag = True
                break
        if flag: break

    for i in range(n):
        for j in range(m):
            if i1 <= i <= i2 and j1 <= j <= j2:
                if s[i][j] != 'X':
                    return False
            else:
                if s[i][j] == 'X':
                    return False
    return True


if check():
    print('YES')
else:
    print('NO')
