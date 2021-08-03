n = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(n - 1):
    if A[i + 1] >= A[i]:
        pass
    elif A[i + 1] < A[i]:
        ans += A[i] - A[i + 1]
        A[i + 1] += A[i] - A[i + 1]

print(ans)
