m = 998244353
n, *d = map(int, open(0).read().split())
a = s = 1
n -= 1
for v in d:
    a = a * v % m
    s += v - 1
while n := n - 1:
    a = a * (s - n) % m
print(a)
