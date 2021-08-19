import sys
l = input()
n = len(l)
mod = pow(10, 9) + 7
sys.setrecursionlimit(10 ** 7)
(dp1, dp2) = (0, 1)
for i in range(n):
    if l[i] == '0':
        dp1 *= 3
    else:
        dp1 *= 3
        dp1 += dp2
        dp2 *= 2
    dp1 %= mod
    dp2 %= mod
print((dp1 + dp2) % mod)
