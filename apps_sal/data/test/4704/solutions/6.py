N = int(input())
A = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    A[i] = A[i] + A[i - 1]
ans = float('inf')
for i in range(1, N):
    ans = min(ans, abs(A[N] - 2 * A[i]))
print(ans)
