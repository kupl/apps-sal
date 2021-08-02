n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += B[A[i] - 1]
    if i < n - 1 and A[i] + 1 == A[i + 1]:
        ans += C[A[i] - 1]
print(ans)
