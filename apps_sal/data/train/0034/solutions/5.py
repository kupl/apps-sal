import sys
input = sys.stdin.readline
def getInt(): return int(input())
def getVars(): return list(map(int, input().split()))
def getList(): return list(map(int, input().split()))
def getStr(): return input().strip()


t = getInt()
for _ in range(t):
    n = getInt()
    if n % 2 == 1:
        print('7' + '1' * (n // 2 - 1))
    else:
        print('1' * (n // 2))
