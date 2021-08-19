(n, *d) = map(int, open(0).read().split())
(a, m, s) = (1, 998244353, sum(d))
d.extend(range(s - 2 * n + 3, s - n + 1))
for i in d:
    a = a * i % m
print(a)
