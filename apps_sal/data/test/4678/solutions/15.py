N = int(input())
A = list(map(int, input().split()))

max_n = A[0]
ans = 0
for i in range(N):
    tmp = max_n - A[i]
    if tmp > 0:
        ans += tmp
    if max_n < A[i]:
        max_n = A[i]
print(ans)
