N, M = map(int, input().split())
print(((N - M) * 100 + 1900 * M) * (2**M))
