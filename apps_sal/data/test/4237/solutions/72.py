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
    A, B, C, D = LI()

    # X以下の自然数でCでもDでも割り切れないものの個数
    def f(X):
        ret = X - X // C - X // D + X // (C * D // math.gcd(C, D))
        return ret

    ans = f(B) - f(A - 1)
    print(ans)

def __starting_point():
    resolve()

__starting_point()
