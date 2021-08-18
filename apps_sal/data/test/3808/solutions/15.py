import sys
input = sys.stdin.readline


def getInt(): return int(input())
def getVars(): return list(map(int, input().split()))
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
s = getStr()
if n % 2 == 1:
    r = 'No'
else:
    r = 'Yes'
    num = 0
    for i in range(n):
        if s[i] == '(':
            num += 1
        else:
            num -= 1
            if num < -1:
                r = 'No'
                break
    if num != 0:
        r = 'No'
print(r)
