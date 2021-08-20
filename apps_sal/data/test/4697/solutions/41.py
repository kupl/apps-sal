(N, M) = list(map(int, input().split()))
if N * 2 >= M:
    print(int(M / 2))
else:
    x = (M - 2 * N) / 4
    N += int(x)
    M -= 2 * int(x)
    print(N)
