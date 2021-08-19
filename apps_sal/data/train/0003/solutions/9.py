def main():
    (N, K) = list(map(int, input().split()))
    (*A,) = list(map(int, input().split()))
    A.sort()
    print(A[-1] + sum(A[-K - 1:-1]))


def __starting_point():
    for __ in [0] * int(input()):
        main()


__starting_point()
