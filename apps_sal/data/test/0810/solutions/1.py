from bisect import bisect_right, bisect_left
(a, b, n) = map(int, input().split())
if a > b:
    (a, b) = (b, a)
(u, v) = (10 * a, 10 * b)
(x, y) = (a * n, b * n)
(t, d) = ([a, b], b - a)
while t[-1] < x:
    t = [j + u for j in t] + [j + v for j in t]
    (u, v) = (u * 10, v * 10)
if t[-1] < y:
    t += [j + u for j in t] + [j + v for j in t]
(t, s) = (t[bisect_left(t, x):bisect_right(t, y)], 0)
(m, f) = (1000000007, [1] + [0] * n)
(p, k) = (list(range(x, y + 1, d)), 0)
for i in range(1, n + 1):
    f[i] = f[i - 1] * i % m
for i in t:
    k = bisect_left(p, i)
    if p[k] == i:
        s += pow(f[k] * f[n - k], m - 2, m)
print(s % m * f[n] % m)
