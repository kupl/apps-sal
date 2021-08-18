def __starting_point():

    k, n = list(map(int, input().split()))
    A = list(map(int, input().split()))

    sbn = -1
    for i in range(n - 1):
        sbn = max(sbn, A[i + 1] - A[i])

    tmp1 = A[0] - 0
    tmp2 = k - A[n - 1]
    sbn = max(sbn, tmp1 + tmp2)

    print((k - sbn))


__starting_point()
