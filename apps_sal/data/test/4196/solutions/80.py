from math import *

n = int(input())
a = list(map(int, input().split()))

l = [a[0]]
for i in range(1, n - 1):
    l.append(gcd(a[i], l[i - 1]))

ans = l[n - 2]
r = a[n - 1]
for i in range(n - 2, 0, -1):
    r = gcd(r, a[i + 1])
    ans = max(ans, gcd(l[i - 1], r))
ans = max(ans, gcd(r, a[1]))
print(ans)
