n, k = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for j in range(1, n):
    if A[j] + A[j - 1] < k:
        ans += k - A[j] - A[j - 1]
        A[j] += k - A[j] - A[j - 1]

print(ans)
print(' '.join(map(str, A)))
