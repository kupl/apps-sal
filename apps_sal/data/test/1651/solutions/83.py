import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    S, P = list(map(int, input().split()))

    cand = []
    for i in range(1, int(P ** 0.5) + 1):
        if P % i == 0:
            cand.append((i, P // i))

    for n, m in cand:
        if n + m == S:
            print("Yes")
            return

    print("No")


def __starting_point():
    main()


__starting_point()
