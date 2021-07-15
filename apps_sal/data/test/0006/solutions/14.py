import sys
input = sys.stdin.readline
 
def getInt(): return int(input())
def getVars(): return list(map(int, input().split()))
def getList(): return list(map(int, input().split()))
def getStr(): return input().strip()
## -------------------------------
 
def addDictList(d, key, val):
    if key not in d: d[key] = []
    d[key].append(val)
 
def addDictInt(d, key, val):
    if key not in d: d[key] = 0
    d[key] = val
    
def addDictCount(d, key):
    if key not in d: d[key] = 0
    d[key] += 1
 
def addDictSum(d, key, val):
    if key not in d: d[key] = 0
    d[key] += val
 
## -------------------------------
 
t = getInt()
for _ in range(t):
    n, x = getVars()
    razn = 0
    maxD = 0
    for i in range(n):
        d, h = getVars()
        razn = max(razn, d-h)
        maxD = max(d, maxD)
    if razn == 0:
        if maxD < x:
            print(-1)
        else:
            print(1)        
    else:
        x = max(x-maxD, 0)
        if x == 0:
            print(1)
        else:
            res = x // razn
            if x == res*razn:
                print(res+1)
            else:
                print(res+2)
                

