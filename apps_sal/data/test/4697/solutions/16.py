N, M = (int(T) for T in input().split())
if 2 * N < M:
    print(N + (M - 2 * N) // 4)
else:
    print(M // 2)
