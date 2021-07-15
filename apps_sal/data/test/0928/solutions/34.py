import bisect
N, K = map(int, input().split())
A = list(map(int, input().split()))
C = [0] * N
C[0] = A[0]
for i in range(1, N):
    C[i] = C[i-1] + A[i]

ans = 0
for i in range(N):
    x = 0 if i == 0 else C[i-1]
    ans += N - bisect.bisect_left(C, K + x)
print(ans)
