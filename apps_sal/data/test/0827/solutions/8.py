import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 50
n = I()
t = S()
if n == 1:
    if t == '0':
        print((10 ** 10))
    else:
        print((2 * 10**10))
elif '00' in t or '010' in t or '111' in t:
    print((0))
else:
    start = t[:2]
    if start == '11':
        if n % 3 == 0:
            print((10**10 - n // 3 + 1))
        else:
            print((10**10 - n // 3))
    elif start == '10':
        print((10**10 - n // 3))
    else:
        if n % 3 == 2:
            print((10**10 - n // 3 - 1))
        else:
            print((10**10 - n // 3))
