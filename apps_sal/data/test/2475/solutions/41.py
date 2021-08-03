n, *s = map(int, open(0).read().split())
a = 0
for i in range(1, n):
    t = 0
    for j in range(0, [n // 2, n + ~i][(n - 1) % i > 0], i):
        t += s[j] + s[~j]
        a = max(a, t)
print(a)
