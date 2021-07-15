n, x = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    if A[i] + A[i + 1] > x:
        ans += A[i] + A[i + 1] - x
        A[i + 1] = max(x - A[i], 0)
print(ans)
