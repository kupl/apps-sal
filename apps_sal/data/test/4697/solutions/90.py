(N, M) = list(map(int, input().split()))
if N * 2 > M:
    print(M // 2)
elif N * 2 == M:
    print(N)
else:
    count = N
    M -= 2 * N
    count += M // 4
    print(count)
