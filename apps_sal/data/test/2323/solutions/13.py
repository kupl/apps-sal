from bisect import bisect_left as j
(k, w, b) = (input, int, sorted)


def f():
    return map(w, k().split())


n = w(k())
s = b([*f()])
(e, c) = (b((x - s[i - 1] for (i, x) in enumerate(s) if i > 0)), [0] * n)
for i in range(n - 1):
    c[i + 1] = c[i] + e[i]
for _ in range(w(k())):
    (l, r) = f()
    i = j(e, r - l + 1)
    print((r - l + 1) * (n - i) + c[i], end=' ')
