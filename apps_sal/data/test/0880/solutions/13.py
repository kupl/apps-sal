"""
Spyder Editor

This is a temporary script file.
"""
mod = 998244353
n = int(input())
a = []
i = 1
a.append(0)
a.append(n)
ans = n
for i in range(1, n):
    ans = ((ans % mod) * (n - i)) % mod
    a.append(ans)
ans = 0
for i in a:
    ans = (ans % mod + a[-1] % mod - i % mod) % mod
print(ans)
