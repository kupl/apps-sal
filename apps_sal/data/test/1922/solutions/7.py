(N, M) = list(map(int, input().split()))
if N > 1 and M > 1:
    print((N - 2) * (M - 2))
else:
    print(abs(max([M, N]) - 2))
