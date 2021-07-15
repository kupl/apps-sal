import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def fact_mod(n, MOD):
    ret = 1
    for i in range(1, n + 1):
        ret *= i
        ret %= MOD
    return ret

def resolve():
    N, M = LI()

    if N == M:
        ans = 2 * pow(fact_mod(N, MOD), 2, MOD)
        ans %= MOD
        print(ans)
    elif abs(N - M) <= 1:
        ans = fact_mod(N, MOD) * fact_mod(M, MOD)
        ans %= MOD
        print(ans)
    else:
        print((0))


def __starting_point():
    resolve()

__starting_point()
