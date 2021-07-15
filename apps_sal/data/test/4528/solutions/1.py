import sys
input = sys.stdin.readline
def getInt(): return int(input())
def getVars(): return list(map(int, input().split()))
def getList(): return list(map(int, input().split()))
def getStr(): return input().strip()
## -------------------------------

t= getInt()
for _ in range(t):
    h, m = getVars()
    print(60*24 - h*60 - m)


