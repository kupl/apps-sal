import sys
input = sys.stdin.readline


def getInt(): return int(input())
def getVars(): return map(int, input().split())
def getList(): return list(map(int, input().split()))
def getStr(): return input().strip()


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


n = getInt()
d = getInt()
e = getInt()

m1 = max(d, e * 5)
m2 = min(d, e * 5)


res = n % m1
for x in range(n // m1 + 1):
    res = min(res, (n - x * m1) % m2)
print(res)
