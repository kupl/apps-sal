N, M = [int(i) for i in input().split()]
if 2 * N >= M:
    print((M // 2))
else:
    print((N + (M - N - N) // 4))

