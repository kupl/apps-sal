import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()
def print(x): return sys.stdout.write(f"{x}\n")


dp = 0


def LCS(str1, str2):
    XY = 0
    nonlocal dp
    _max = -1
    len1, len2 = len(str1), len(str2)
    dp = [[0 for x in range(len1 + 1)] for x in range(len2 + 1)]
    for x in range(1, len2 + 1):
        for y in range(1, len1 + 1):
            if str2[x - 1] == str1[y - 1]:
                dp[x][y] = dp[x - 1][y - 1] + 1
            else:
                dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])
            if _max < dp[x][y]:
                _max = dp[x][y]
                XY = [x, y]
    return (_max, XY)


def LCSSTRING(str1, str2, XY, answer):
    nonlocal dp
    X, Y = XY[0], XY[1]
    if dp[X][Y] == 0:
        return answer
    if str2[X - 1] == str1[Y - 1]:
        answer = str2[X - 1] + answer
        XY[0] -= 1
        XY[1] -= 1
    else:
        if dp[X - 1][Y] > dp[X][Y - 1]:
            XY[0] -= 1
        else:
            XY[1] -= 1
    return LCSSTRING(str1, str2, XY, answer)


for t in range(int(input())):
    s, t, p = input(), input(), input()

    m, xy = LCS(s, t)
    lcs = LCSSTRING(s, t, xy, "")

    if lcs != s:
        print("NO")
        continue

    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for i in t:
        d1[i] += 1
    for i in p:
        d2[i] += 1
    for i in lcs:
        d2[i] += 1

    flag = True
    for i in t:
        if d1[i] > d2[i]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
