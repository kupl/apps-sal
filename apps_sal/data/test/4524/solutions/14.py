import sys
(n, m) = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().strip()))
b = list(map(int, sys.stdin.readline().strip()))
mod = 998244353
ANS = 0
for i in range(1, m):
    b[i] = b[i - 1] + b[i]
if m >= n:
    b = b[-n:]
else:
    a = a[-m:]
    n = m
A = [a[i] * b[i] for i in range(n)]
A.reverse()
for i in range(n):
    ANS = (ANS + pow(2, i, mod) * A[i]) % mod
print(ANS)
