N, M = map(int, input().split())

print(int((M * 1900 + (N - M) * 100) * 2**M))
