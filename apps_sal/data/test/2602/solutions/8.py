mod = 1000000007
eps = 10 ** (-9)


def main():
    import sys
    input = sys.stdin.readline
    for _ in range(int(input())):
        (A, B, N, M) = list(map(int, input().split()))
        if A + B < N + M:
            print('No')
        else:
            mi = min(A, B)
            if mi < M:
                print('No')
            else:
                print('Yes')


def __starting_point():
    main()


__starting_point()
