import sys
sys.setrecursionlimit(10**6)


def __starting_point():
    nofkase = int(input())
    for kase in range(nofkase):
        n = int(input())
        n = n // 2
        print(n * (n + 1) * (n + n + 1) * 8 // 6)


__starting_point()
