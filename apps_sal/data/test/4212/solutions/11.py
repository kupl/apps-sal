import itertools
(n, m, q) = map(int, input().split())
(a, b, c, d) = ([0] * q, [0] * q, [0] * q, [0] * q)
for i in range(q):
    (a[i], b[i], c[i], d[i]) = map(int, input().split())
ans = 0
for C in itertools.combinations_with_replacement(range(1, m + 1), n):
    x = 0
    for i in range(q):
        if C[b[i] - 1] - C[a[i] - 1] == c[i]:
            x += d[i]
    ans = max(ans, x)
print(ans)
