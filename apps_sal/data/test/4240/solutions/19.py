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
    S = SS()
    T = SS()
    l = len(S)
    S2 = S * 2

    ans = 'No'
    for i in range(l):
        if S2[i:i+l] == T:
            ans = 'Yes'
            break

    print(ans)

def __starting_point():
    resolve()

__starting_point()
