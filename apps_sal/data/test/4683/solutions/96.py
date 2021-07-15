import sys

N = int(input())
A = list(map(int, input().split()))

sum = [A[N-1]]
ans = 0
for i in range(1, N):
    ans += A[N-i-1]*sum[-1]%(10**9+7)
    ans %= (10**9+7)
    sum.append((sum[-1]+A[N-i-1])%(10**9+7))
print(ans)

