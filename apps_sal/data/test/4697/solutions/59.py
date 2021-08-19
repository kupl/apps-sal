(N, M) = list(map(int, input().split()))
A = 0
if 2 * N <= M:
    A += N
    M -= 2 * N
    print(A + M // 4)
else:
    print(M // 2)
