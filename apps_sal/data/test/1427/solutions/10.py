from math import gcd
n = int(input())
a = list(map(int, input().split()))
x = a[0]
mod = 10 ** 9 + 7
for i in range(1, n):
    x = x * a[i] // gcd(x, a[i])
ans = 0
for i in range(n):
    ans += x // a[i]
print(ans % mod)
