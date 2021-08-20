import bisect


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


(n, k, d) = getIntList()
a = getIntList()
a.sort()
seen = [False] * len(a)


def search(a, lowLim):
    sameLim = bisect.bisect_right(a, a[lowLim] + d)
    lowLim = max(lowLim, sameLim - 2 * k)
    if seen[lowLim]:
        return False
    if len(a) - lowLim < k:
        return False
    if a[len(a) - 1] - a[lowLim] <= d:
        return True
    for i in range(lowLim + k - 1, len(a) - 1):
        if a[i] - a[lowLim] > d:
            break
        if search(a, i + 1):
            return True
    seen[lowLim] = True
    return False


def searchFull(a):
    if a[n - 1] - a[n - k] > d:
        return False
    return search(a, 0)


if k == 1:
    print('YES')
elif searchFull(a):
    print('YES')
else:
    print('NO')
