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
    A = LI()
    A_abs = [abs(i) for i in A]

    if len([i for i in A if i < 0]) % 2 == 1:
        ans = sum(A_abs) - 2 * min(A_abs)
    else:
        ans = sum(A_abs)

    print(ans)

def __starting_point():
    resolve()

__starting_point()
