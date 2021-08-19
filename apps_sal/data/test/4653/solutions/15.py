import sys
input = sys.stdin.readline
def getInt(): return int(input())
def getVars(): return list(map(int, input().split()))
def getList(): return list(map(int, input().split()))
def getStr(): return input().strip()
# -------------------------------


t = getInt()
for _ in range(t):
    n, k = getVars()
    m = n // k
    if m * k == n:
        print(n)
        continue
    m1 = k // 2
    res = min(n, m * k + m1)
    print(res)
