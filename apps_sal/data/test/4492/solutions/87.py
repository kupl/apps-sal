(N, x) = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
if A[0] > x:
    ans += A[0] - x
    A[0] = x
for i in range(1, N):
    if A[i] + A[i - 1] > x:
        ans += A[i] + A[i - 1] - x
        A[i] -= A[i] + A[i - 1] - x
print(ans)
