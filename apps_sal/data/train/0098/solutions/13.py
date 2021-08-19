import sys
input = sys.stdin.readline


def getInt():
    return int(input())


def getVars():
    return list(map(int, input().split()))


def getList():
    return list(map(int, input().split()))


def getStr():
    return input().strip()


def addDictList(d, key, val):
    if key not in d:
        d[key] = []
    d[key].append(val)


def addDictInt(d, key, val):
    if key not in d:
        d[key] = 0
    d[key] = val


def addDictCount(d, key):
    if key not in d:
        d[key] = 0
    d[key] += 1


def addDictSum(d, key, val):
    if key not in d:
        d[key] = 0
    d[key] += val


t = getInt()
for _ in range(t):
    (c, m, x) = getVars()
    res = min(c, m)
    res = min(res, (c + m + x) // 3)
    print(res)
