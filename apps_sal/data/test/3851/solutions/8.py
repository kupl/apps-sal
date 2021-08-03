from math import gcd
n, k = map(int, input().split())
a, b = map(int, input().split())
t = n * k
m = [(a + b) % k, (a - b) % k, (b - a) % k, (-a - b) % k]
mi = 999999999999
ma = 0
for i in range(n):
    for c in m:
        l = i * k + c
        mi = min(t // gcd(t, l), mi)
        ma = max(t // gcd(t, l), ma)
print(mi, ma)
