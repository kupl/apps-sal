from math import gcd
n = int(input())
a = list(map(int, input().split()))
t = a[0]
for i in range(1, n):
    t = t * a[i] // gcd(t, a[i])
ans = 0
for i in a:
    ans += (t - 1) % i
print(ans)
