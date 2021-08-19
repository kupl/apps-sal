(N, M) = map(int, input().split())
if N <= M // 2:
    print(N + (M - 2 * N) // 4)
else:
    print(M // 2)
