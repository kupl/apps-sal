import sys
input = sys.stdin.readline
(n, m, L, R) = list(map(int, input().split()))
mod = 998244353
ANS = pow(R - L + 1, n * m, mod)
if n * m % 2 == 1:
    print(ANS)
elif (R - L + 1) % 2 == 0:
    print(ANS * pow(2, mod - 2, mod) % mod)
else:
    print((ANS + 1) * pow(2, mod - 2, mod) % mod)
