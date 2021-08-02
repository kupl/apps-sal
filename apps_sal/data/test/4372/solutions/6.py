from math import gcd
n = int(input())
a = list(map(int, input().split()))
d = max(a)
s = 0
k = 0
for i in range(n):
    s += d - a[i]
    k = gcd(k, d - a[i])
print(s // k, k)
