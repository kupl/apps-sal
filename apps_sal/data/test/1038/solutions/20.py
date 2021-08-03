# 54
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


def ruiseki_xor(n):
    if n % 2 != 0:
        if (n + 1) // 2 % 2 == 0:
            return 0
        else:
            return 1
    # n は偶数
    return ruiseki_xor(n + 1) ^ (n + 1)


a, b = LI()
# a から b の 和 : (bまでの和) - (a - 1 までの和)
ans = ruiseki_xor(b) ^ ruiseki_xor(a - 1)
print(ans)
