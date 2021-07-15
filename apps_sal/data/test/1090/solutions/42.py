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
    N, K = LI()
    S = SS()

    # 最初の幸福度
    h = 0
    for i in range(N - 1):
        if S[i] == S[i+1]:
            h += 1

    # YX...XYに対して操作をすると幸福人数を2増やせる
    # 端X...XYに対して操作をすると幸福人数を1増やせる
    cnt = 0
    for i in range(N - 1):
        if S[i] != S[i+1]:
            cnt += 1

    if cnt >= 2 * K:
        h += 2 * K
    else:
        h = N - 1 

    print(h)

def __starting_point():
    resolve()

__starting_point()
