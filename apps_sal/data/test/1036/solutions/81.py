import bisect, collections, copy, functools, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    n, k = LI()
    s = SS()
    s = s * 2
    d = {'R': 0, 'P': 1, 'S': 2}
    d_r = {0: 'R', 1: 'P', 2: 'S'}

    dp = [[-1] * n for _ in range(k + 1)]
    # k: 木の高さ i: sの左からのオフセット
    def f(k, i):
        if dp[k][i] == -1:
            if k == 0:
                dp[k][i] = d[s[i]]
            else:
                l = f(k - 1, i)
                r = f(k - 1, (i + pow(2, k - 1, n)) % n)
                if l == r or (l - r) % 3 == 1:
                    dp[k][i] = l
                else:
                    dp[k][i] = r
        return dp[k][i]

    f(k, 0)
    print((d_r[dp[k][0]]))

def __starting_point():
    resolve()

__starting_point()
