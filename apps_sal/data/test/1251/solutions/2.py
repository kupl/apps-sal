import sys
sys.setrecursionlimit(10000)
(s, n) = (1, int(input()))
t = [(q, i) for (i, q) in enumerate(map(int, input().split()))]
e = (2000000000.0, 0)
while s < n:
    s <<= 1
h = [e] * s + t + [e] * (s - n)
k = s - 1
while k:
    j = k << 1
    h[k] = min(h[j], h[j + 1])
    k -= 1


def f(a, l, r):
    if r - l < 1:
        return 0
    if r - l < 2:
        return int(t[l][0] != a)
    (p, q) = ([(s, l, r)], e)
    while p:
        (k, u, v) = p.pop()
        if u < v:
            if u & 1:
                q = min(q, h[k + u])
                u += 1
            if v & 1:
                q = min(q, h[k + v - 1])
            p.append((k >> 1, u >> 1, v >> 1))
    (b, m) = q
    (d, n) = (b - a, r - l)
    return min(n, d + f(b, l, m) + f(b, m + 1, r)) if d < n else n


print(f(0, 0, n))
