(N, M) = list(map(int, input().split()))
print((1900 * M + 100 * (N - M)) * 2 ** M)
