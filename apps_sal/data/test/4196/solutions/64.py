from math import gcd
n = int(input())
a = [*map(int, input().split())]
lgcd = [0] * (n + 2)
rgcd = [0] * (n + 2)
for i in range(n):
    lgcd[i + 1] = gcd(lgcd[i], a[i])
    rgcd[n - i] = gcd(rgcd[n - i + 1], a[n - i - 1])
ans = 0
for i in range(n + 1):
    ans = max(ans, gcd(lgcd[i - 1], rgcd[i + 1]))
print(ans)
