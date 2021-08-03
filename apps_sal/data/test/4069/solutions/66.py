import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    X, K, D = list(map(int, input().split()))
    if abs(K * D) < abs(X):
        print((abs(X) - abs(K * D)))
    else:
        m = X // D
        x = X - m * D
        k = K - m
        if k % 2 == 0:
            print((abs(x)))
        else:
            print((abs(x - D)))


def __starting_point():
    main()


__starting_point()
