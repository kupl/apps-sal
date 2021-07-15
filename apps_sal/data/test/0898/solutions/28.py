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

    M_div = []
    for i in range(1, int(M ** 0.5) + 1):
        if M % i == 0:
            M_div.append(i)
            M_div.append(M // i)

    # Mの約数の中でMを割った時の値がN以上になるような最大のもの
    ans = 1
    for i in M_div:
        if M // i >= N:
            ans = max(i, ans)

    print(ans)

def __starting_point():
    resolve()

__starting_point()
