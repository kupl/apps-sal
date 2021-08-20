(N, K, M) = map(int, input().split())
A = list(map(int, input().split()))
if M * N - sum(A) <= K:
    print(max(M * N - sum(A), 0))
else:
    print(-1)
