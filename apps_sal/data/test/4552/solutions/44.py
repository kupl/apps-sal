import sys
from heapq import heappush, heappop
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


def main():
    n = ii()
    F = []
    P = []
    for _ in range(n):
        F.append(li())
    for _ in range(n):
        P.append(li())

    inf = 10 ** 18
    ans = -inf
    for i in range(1, 1 << 10):
        c = [0] * (n)
        tmp = 0
        for j in range(10):
            if (i >> j) & 1:
                for k in range(n):
                    c[k] += F[k][j]
        for k in range(n):
            tmp += P[k][c[k]]
        ans = max(ans, tmp)
    print(ans)


def __starting_point():
    main()


__starting_point()
