from math import *
N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 1
M = 10**9 + 7
p = 10**K - 1
u = 10**(K - 1)
for i in range(N // K):
    ans *= (p // a[i] + 1 - ((u * (b[i] + 1) + a[i] - 1) // a[i] - (b[i] * u + a[i] - 1) // a[i]))
    ans %= M
print((ans + M) % M)
