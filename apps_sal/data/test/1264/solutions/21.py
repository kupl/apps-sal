(n, t) = (int(input()), list(map(int, input().split())))
k = t.count(1)
p = [0] * n
(s, m) = (0, 0)
for i in range(0, n):
    s += [-1, 1][t[i]]
    t[i] = s
    if s > m:
        m = s
    p[i] = m
(m, s) = (t[-1], p[-1] - t[-1])
for i in range(2, n + 1):
    m = min(t[-i], m)
    d = p[-i] - m
    if s < d:
        s = d
print(k + s - (k == n))
