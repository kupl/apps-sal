N, M = map(int, input().split())
print((100 * (N - M) + 1900 * M) * (2**M))
