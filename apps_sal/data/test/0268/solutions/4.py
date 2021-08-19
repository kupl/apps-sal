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
cuttable = [False] * len(a)
cuttable[0] = True


def search(a):
    curr = 0
    maxOne = 0
    while True:
        if cuttable[curr]:
            lowLim = curr + k
            upLim = bisect.bisect_right(a, a[curr] + d)
            if upLim == len(a):
                return True
            lowLim = max(lowLim, maxOne + 1)
            for i in range(lowLim, upLim + 1):
                cuttable[i] = True
            maxOne = upLim
        curr += 1
        if curr > len(a) - k:
            break
    return False


if k == 1:
    print('YES')
elif search(a):
    print('YES')
else:
    print('NO')
