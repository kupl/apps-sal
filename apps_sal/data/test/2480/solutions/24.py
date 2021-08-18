N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
for i in range(1, N):
    A[i] += A[i - 1]

for i in range(N):
    A[i] -= (i + 1)
    A[i] %= K
A = [0] + A
D = {}
ans = 0
for j in range(1, N + 1):
    D[A[j - 1]] = D.get(A[j - 1], 0) + 1
    if j - K >= 0:
        D[A[j - K]] -= 1
    ans += D.get(A[j], 0)
print(ans)
