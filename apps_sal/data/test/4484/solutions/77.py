import math
n, m = map(int, input().split())
p = 10**9 + 7


nf = math.factorial(n) % p
mf = math.factorial(m) % p

if abs(n - m) > 1:
    ans = 0

elif n == m:
    ans = nf * mf * 2

else:
    ans = nf * mf

print(ans % p)
