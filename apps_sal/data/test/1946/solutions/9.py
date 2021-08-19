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


n = int(input())
(a, x) = getTransIntList(n)
m = int(input())
(b, y) = getTransIntList(m)


def solve():
    d = dict()
    for i in range(n):
        currA = a[i]
        currX = x[i]
        d[currA] = currX
    for j in range(m):
        currB = b[j]
        currY = y[j]
        d[currB] = max(d.get(currB, 0), currY)
    result = 0
    for key in list(d.keys()):
        result += d[key]
    return result


print(solve())
