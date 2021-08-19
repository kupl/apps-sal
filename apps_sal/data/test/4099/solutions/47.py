(N, K, M) = map(int, input().split())
A = list(map(int, input().split()))
if (sum(A) + K) / N < M:
    print(-1)
elif sum(A) / N >= M:
    print(0)
else:
    print(M * N - sum(A))
