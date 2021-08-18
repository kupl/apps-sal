import sys
input = sys.stdin.readline


def getInt(): return int(input())
def getVars(): return list(map(int, input().split()))
def getList(): return list(map(int, input().split()))
def getStr(): return input().strip()


t = getInt()
for _ in range(t):
    n, k, d = getVars()
    a = getList()
    b = {}
    for i in range(d):
        if a[i] not in b:
            b[a[i]] = 0
        b[a[i]] += 1
    res = len(list(b.keys()))
    for i in range(d, n):
        b[a[i - d]] -= 1
        if b[a[i - d]] == 0:
            del b[a[i - d]]
        if a[i] not in b:
            b[a[i]] = 0
        b[a[i]] += 1
        res = min(res, len(list(b.keys())))
    print(res)
