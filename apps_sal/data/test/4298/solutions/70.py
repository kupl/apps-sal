(N, D) = map(int, input().split())
if N % (2 * D + 1):
    print(N // (2 * D + 1) + 1)
else:
    print(N // (2 * D + 1))
