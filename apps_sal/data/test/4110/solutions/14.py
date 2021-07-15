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
    D, G = LI()
    pc = [LI() for _ in range(D)]

    # コンプリートする問題を全パターン試す
    # 足りない分があれば解いてない最高点数の問題で埋める
    ans = sum([i[0] for i in pc])
    for i in range(2 ** D):
        score = 0
        num = 0
        not_completed_max = -1
        for j in range(D):
            if i >> j & 1:
                score += pc[j][0] * (j + 1) * 100  + pc[j][1]
                num += pc[j][0]
            else:
                not_completed_max = max(j, not_completed_max)
        if score >= G:
            ans = min(num, ans)
        elif (G - score) // ((not_completed_max + 1) * 100) <= pc[not_completed_max][0]:
            ans = min(num + (G - score - 1) // ((not_completed_max + 1) * 100) + 1, ans)

    print(ans)

def __starting_point():
    resolve()

__starting_point()
