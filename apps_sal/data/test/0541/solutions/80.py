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
    N, M = LI()
    ab = [LI_() for _ in range(M)]
    ab.sort(key=lambda x: x[1])

    # 区間スケジューリング
    ans = 0
    # print(ab)
    right = -1
    for a, b in ab:
        if right <= a:
            right = b
            ans += 1

    print(ans)

def __starting_point():
    resolve()

__starting_point()
