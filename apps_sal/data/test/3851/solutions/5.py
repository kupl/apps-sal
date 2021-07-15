from math import gcd


n, k = list(map(int, input().split()))
a, b = list(map(int, input().split()))
t = n * k
m = [(a + b) % k, (a - b) % k, (-a + b) % k, (-a - b) % k]
mi = 999999999999999
ma = 0
for i in range(n):
    for c in m:
        L = i * k + c
        mi = min(t // gcd(t, L), mi)
        ma = max(t // gcd(t, L), ma)
print(mi, ma)

