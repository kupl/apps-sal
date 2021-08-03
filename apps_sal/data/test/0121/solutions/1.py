import sys

m = [list(input()) for _ in range(4)]


def trans(m):
    return [[m[0][0], m[1][0], m[2][0], m[3][0]],
            [m[0][1], m[1][1], m[2][1], m[3][1]],
            [m[0][2], m[1][2], m[2][2], m[3][2]],
            [m[0][3], m[1][3], m[2][3], m[3][3]]]


def check(m):
    res = any('xxx' in ''.join(x) for x in m)
    res |= any('xxx' in ''.join(x) for x in trans(m))

    for i in range(1, 3):
        for j in range(1, 3):
            res |= m[i - 1][j - 1] + m[i][j] + m[i + 1][j + 1] == 'xxx'
            res |= m[i - 1][j + 1] + m[i][j] + m[i + 1][j - 1] == 'xxx'

    return res


for i in range(4):
    for j in range(4):
        if m[i][j] == '.':
            m[i][j] = 'x'
            if check(m):
                print("YES")
                return
            m[i][j] = '.'

print("NO")
