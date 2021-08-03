import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()


def resolve():
    S = SS()

    ans = 0
    stk = []
    for i in S:
        if stk and stk[-1] != i:
            stk.pop()
            ans += 2
        else:
            stk.append(i)

    print(ans)


def __starting_point():
    resolve()


__starting_point()
