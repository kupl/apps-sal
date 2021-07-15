N, K, M = map(int, input().split())

A = list(map(int, input().split()))
score = sum(A)

if N * M - score > K:
    print(-1)
else:
    print(max(N * M - score, 0))
