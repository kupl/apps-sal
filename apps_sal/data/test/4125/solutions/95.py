from math import gcd
(n, x) = map(int, input().split())
a = [int(i) - x for i in list(map(int, input().split()))]
now = a[0]
for i in a:
    now = gcd(now, i)
print(now)
