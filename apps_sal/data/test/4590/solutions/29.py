import bisect
(N, M, K) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(1, N):
    A[i] += A[i - 1]
for i in range(1, M):
    B[i] += B[i - 1]
ma = bisect.bisect(A, K)
for m in range(0, M):
    if B[m] > K:
        break
    n = bisect.bisect(A, K - B[m])
    if ma < n + m + 1:
        ma = n + m + 1
print(ma)
