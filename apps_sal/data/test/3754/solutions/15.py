m = 998244353
(n, *d) = map(int, open((y := 0)).read().split())
a = 1
for v in d:
    a = a * v % m
    y += v - 1
for i in range(n - 2):
    a = a * (y - i) % m
print(a)
