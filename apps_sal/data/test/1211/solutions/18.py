def __starting_point():
    (N, K) = map(int, input().split())
    A = list(map(int, input().split()))
    m = 10000000000000000000
    j = 0
    c = 0
    for i in range(K):
        k = N % A[i]
        if k < m:
            m = k
            c = N // A[i]
            j = i + 1
    print(j, c)


__starting_point()
