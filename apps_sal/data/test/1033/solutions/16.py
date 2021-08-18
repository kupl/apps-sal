import math


def getIntList():
    return list(map(int, input().split()))


def getTransIntList(n):
    first = getIntList()
    m = len(first)
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        result[i][0] = first[i]
    for j in range(1, n):
        curr = getIntList()
        for i in range(m):
            result[i][j] = curr[i]
    return result


n, H = getIntList()


def getLim(l):
    if l <= H:
        return l * (l + 1) // 2
    diff = l - H
    x = diff // 2
    if diff % 2 == 0:
        return l * (l + 1) // 2 - x * (x + 1)
    return l * (l + 1) // 2 - (x + 1) * (x + 1)


def solve(n):
    l = 1
    while getLim(l) < n:
        l *= 2
    upLim = l
    lowLim = l // 2
    diff = upLim - lowLim
    while upLim - lowLim > 1:
        curr = (upLim + lowLim) // 2
        if getLim(curr) >= n:
            upLim = curr
        else:
            lowLim = curr
    return upLim


print(solve(n))
