from collections import defaultdict
mod = 10 ** 9 + 7
INF = float('inf')


def getlist():
    return list(map(int, input().split()))


def inverse(N, mod):
    return pow(N, mod - 2, mod)


def main():
    S = list(input())
    N = len(S)
    print(3)
    print('L', N - 1)
    print('R', N - 1)
    print('R', 2 * N - 1)


def __starting_point():
    main()


__starting_point()
