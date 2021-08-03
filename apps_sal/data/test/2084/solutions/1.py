import sys


def solve():
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = sum(a[:k])
    print(ans)


def __starting_point():
    solve()


__starting_point()
