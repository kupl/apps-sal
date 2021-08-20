def __starting_point():
    (N, K, Q) = map(int, input().split())
    A = [0] * N
    for i in range(Q):
        n = int(input())
        A[n - 1] += 1
    for x in A:
        if K - (Q - x) > 0:
            print('Yes')
        else:
            print('No')


__starting_point()
