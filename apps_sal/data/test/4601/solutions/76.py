def main():
    N, K = list(map(int, input().split()))
    H = sorted([int(x) for x in input().split()])

    if K == 0:
        print((sum(H)))
    elif N > K:
        print((sum(H[:-K])))
    else:
        print((0))


def __starting_point():
    main()


__starting_point()
