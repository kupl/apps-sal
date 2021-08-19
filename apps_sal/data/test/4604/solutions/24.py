N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7

A = sorted(A)
ans = 1
if N % 2 == 0:  # [1,1,3,3,5,5,...]
    for i in range(N):
        xx = int(i / 2)
        if A[i] != 2 * xx + 1:
            ans = 0
        else:
            if i % 2 == 1:
                ans *= 2
                ans %= mod
else:  # [0, 2, 2, 4, 4 ...]
    for i in range(N):
        xx = int((i + 1) / 2)
        if A[i] != 2 * xx:
            ans = 0
        else:
            if (i % 2 == 0) and (i != 0):
                ans *= 2
                ans %= mod


print(ans)
