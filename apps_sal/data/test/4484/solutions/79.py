import sys


def LI():
    return list(map(int, input().split()))


N, M = LI()
if abs(N-M) >= 2:
    print((0))
    return
mod = pow(10, 9)+7
x = 1
if N == M:
    for i in range(1, N+1):
        x = (x*i) % mod
    ans = (x*x*2) % mod
else:
    A = max(N, M)
    B = min(N, M)
    for i in range(1, B+1):
        x = (x*i) % mod
    y = (x*A) % mod
    ans = (x*y) % mod
print(ans)

