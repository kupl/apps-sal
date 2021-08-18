def main():
    K = int(input())
    N = 50

    q, r = divmod(K, N)
    a = [x + q for x in range(N)]
    for i in range(N):
        if i < r:
            a[i] += N
            a[i] -= r - 1
        else:
            a[i] -= r

    print(N)
    print((*a))


def __starting_point():
    main()


__starting_point()
