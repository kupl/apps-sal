import sys


def __starting_point():
    N, K = map(int, input().split())

    if N % K == 0:
        print('0')
        return

    N = N % K

    while(N > abs(N - K)):
        N = abs(N - K)

    print(N)


__starting_point()
