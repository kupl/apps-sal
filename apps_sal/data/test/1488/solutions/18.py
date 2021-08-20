from math import gcd
n = int(input())
a = sorted(map(int, input().split()))
ans = 0
for i in range(n):
    ans += 2 * (i + i - n + 1) * a[i]
ans += sum(a)
tmp = gcd(ans, n)
print(ans // tmp, n // tmp)
