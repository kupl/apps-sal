import sys
input = sys.stdin.readline


def getInt(): return int(input())
def getVars(): return list(map(int, input().split()))
def getList(): return list(map(int, input().split()))
def getStr(): return input().strip()


t = getInt()

for _ in range(t):
    r, g, b = getVars()
    a = max(r, g, b)
    c = min(r, g, b)
    b = r + g + b - a - c
    if a <= b + c + 1:
        print('Yes')
    else:
        print('No')
