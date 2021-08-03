import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()


def resolve():
    N = I()
    a = [I() - 1 for _ in range(N)]

    c = 0
    ans = 0
    is_ok = True
    while True:
        c = a[c]
        ans += 1
        if c == 0 or ans > N:
            is_ok = False
            break
        if c == 1:
            break

    if is_ok:
        print(ans)
    else:
        print(-1)


def __starting_point():
    resolve()


__starting_point()
