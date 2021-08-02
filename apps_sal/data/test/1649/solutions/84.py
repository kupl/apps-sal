import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    A, B, C, D = list(map(int, input().split()))
    for i in range(2 ** 4):
        eat = 0
        rest = 0
        for j, x in enumerate([A, B, C, D]):
            if i & (1 << j):
                eat += x
            else:
                rest += x

        if eat == 0:
            continue

        if eat == rest:
            print("Yes")
            return
    else:
        print("No")


def __starting_point():
    main()


__starting_point()
