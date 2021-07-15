import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N = I()
    K = I()
    x = LI()

    ans = sum([2 * min(x[i], K - x[i]) for i in range(N)])
    print(ans)

def __starting_point():
    resolve()
__starting_point()
