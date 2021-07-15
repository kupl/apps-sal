N, M, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
for i in range(1, N+1):
    A[i] += A[i-1]

i = N
total = 0
ans = 0
for j in range(M+1):
    total += B[j]
    while i >= 0 and A[i]+total > K:
        i -= 1
    if A[i]+total <= K:
        ans = max(ans, i+j)

print(ans)
