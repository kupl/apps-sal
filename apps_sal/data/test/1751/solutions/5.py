from sys import stdin
input = stdin.readline
n = int(input())
(res1, res2) = (1, 0)
mod = 1000000007
for x in range(2, n + 1):
    res1 = res1 * x % mod
res2 = pow(2, n - 1, mod)
print((res1 - res2) % mod)
