import numpy as np


def INT():
    return int(input())


def INTM():
    return map(int, input().split())


def STRM():
    return map(str, input().split())


def STR():
    return str(input())


def LIST():
    return list(map(int, input().split()))


def LISTS():
    return list(map(str, input().split()))


def do():
    (h, w) = INTM()
    ban = np.zeros((h, w), dtype=np.int16)
    for i in range(h):
        s = STR()
        for i1 in range(len(s)):
            if s[i1] == '.':
                ban[i][i1] = 1
    left = np.zeros((h, w), dtype=np.int16)
    right = np.zeros((h, w), dtype=np.int16)
    up = np.zeros((h, w), dtype=np.int16)
    down = np.zeros((h, w), dtype=np.int16)
    for i in range(w):
        i2 = w - 1 - i
        if i == 0:
            left[:, i] = ban[:, i]
            right[:, i2] = ban[:, i2]
        else:
            left[:, i] = ban[:, i] * (left[:, i - 1] + 1)
            right[:, i2] = ban[:, i2] * (right[:, i2 + 1] + 1)
    for i in range(h):
        i2 = h - 1 - i
        if i == 0:
            up[i, :] = ban[i, :]
            down[i2, :] = ban[i2, :]
        else:
            up[i, :] = ban[i, :] * (up[i - 1, :] + 1)
            down[i2, :] = ban[i2, :] * (down[i2 + 1, :] + 1)
    anslist = down + up + right + left
    ans = 0
    for i in anslist:
        ans = max(ans, max(i))
    print(ans - 3)


def __starting_point():
    do()


__starting_point()
