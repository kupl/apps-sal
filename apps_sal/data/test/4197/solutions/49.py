def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [[a, i + 1] for (i, a) in enumerate(A)]
    B.sort()
    for (i, j) in B:
        if i == N:
            print(j)
        else:
            print(j, '', end='')


def __starting_point():
    main()


__starting_point()
