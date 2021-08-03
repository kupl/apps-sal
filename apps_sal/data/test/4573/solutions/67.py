def main():
    N = int(input())
    X = list(map(int, input().split()))
    Y = X.copy()
    Y.sort()

    if N % 2 == 0:
        mid1 = Y[N // 2]
        mid2 = Y[N // 2 - 1]
        for x in X:
            if x <= mid2:
                print(mid1)
            else:
                print(mid2)
        return


def __starting_point():
    main()


__starting_point()
