import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()

    # 引き出せる金額リスト
    l = [1]
    a = 6
    b = 9
    while a <= N or b <= N:
        if a < b:
            l.append(a)
            a *= 6
        else:
            l.append(b)
            b *= 9

    # ナップザック
    dp = [INF] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in l:
            if i - j >= 0:
                dp[i] = min(dp[i - j] + 1, dp[i])

    print((dp[-1]))

def __starting_point():
    resolve()

__starting_point()
