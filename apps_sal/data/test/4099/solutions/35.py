N, K, M = map(int, input().split())
*A, = map(int, input().split())
x = N * M - sum(A)
print(-1 if x > K else max(0, x))
