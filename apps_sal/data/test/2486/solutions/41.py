import sys
input = sys.stdin.readline
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = N
total = 0
for i in range(N):
    a = A[N - 1 - i]
    if total + a < K:
        total += a
    else:
        ans = min(ans, N - 1 - i)
print(ans)
