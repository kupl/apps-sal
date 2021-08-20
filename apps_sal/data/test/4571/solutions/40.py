(N, M) = list(map(int, input().split()))
print(M * 1900 * 2 ** M + (N - M) * 100 * 2 ** M)
