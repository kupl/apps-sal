import sys
input = sys.stdin.readline


def getInt(): return int(input())
def getVars(): return list(map(int, input().split()))
def getList(): return list(map(int, input().split()))
def getStr(): return input().strip()

# -------------------------------


a = getInt()
b = getInt()
c = getInt()
d = getInt()
e = getInt()
f = getInt()
res = 0
if (e > f):
    res += min(a, d) * e
    res += min(b, c, d - min(a, d)) * f
else:
    res += min(b, c, d) * f
    res += min(a, d - min(b, c, d)) * e
print(res)
