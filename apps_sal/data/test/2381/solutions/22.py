import sys

mod = 10 ** 9 + 7
N, K = map(int,input().split())
A = list(map(int,input().split()))
if all([a < 0 for a in A]):
    if K % 2 == 0:
        A.sort()
        ans = 1
        for i in range(K):
            ans *= A[i]
            ans %= mod
        print(ans)
        return
    else:
        A.sort(reverse = True)
        ans = 1
        for i in range(K):
            ans *= A[i]
            ans %= mod
        print(ans)
        return

A.sort()
l = 0
r = N - 1
ans = 1

if K % 2 == 1:
    ans *= A[r]
    ans %= mod
    r -= 1

for _ in range(K // 2):
    if A[l] * A[l+1] >= A[r] * A[r-1]:
        ans *= A[l] * A[l+1]
        ans %= mod
        l += 2
    else:
        ans *= A[r] * A[r-1]
        ans %= mod
        r -= 2

print(ans)
