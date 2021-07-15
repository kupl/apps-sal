from bisect import bisect
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
SA = [0] * (N + 1)
SB = [0] * (M + 1)
for i in range(N):
    SA[i+1] = SA[i] + A[i]
for i in range(M):
    SB[i+1] = SB[i] + B[i]
result = 0
for x in range(N+1):
    if SA[x] > K:
        break
    y = bisect(SB, K - SA[x]) - 1
    result = max(result, x + y)
print(result)
