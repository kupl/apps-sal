(n, k) = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    if A[i] + A[i + 1] < k:
        ans += k - (A[i] + A[i + 1])
        A[i + 1] += k - (A[i] + A[i + 1])
print(ans)
for i in range(n):
    print(A[i], end=' ')
