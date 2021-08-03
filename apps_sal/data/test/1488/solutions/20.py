import math

n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

ans = 0
gg = 0
for i in range(n):
    ans += i * a[i] - gg
    gg += a[i]

ans = sum(a) + 2 * ans
g = math.gcd(ans, n)
ans //= g
n //= g
print(ans, n)
