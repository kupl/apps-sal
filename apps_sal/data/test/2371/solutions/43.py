def main():
    (N, Z, W) = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    if N == 1:
        print(abs(A[0] - W))
    else:
        print(max([abs(A[-1] - W), abs(A[-2] - A[-1])]))


def __starting_point():
    main()


__starting_point()
