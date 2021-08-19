xs = input().split()
(n, p, t) = (int(xs[0]), float(xs[1]), int(xs[2]))
(cur, nxt) = ([0.0] * (n + 1), [0.0] * (n + 1))
cur[0] = 1.0
for i in range(t):
    nxt[n] = cur[n]
    for j in range(n):
        nxt[j] = cur[j] * (1.0 - p)
    for j in range(n):
        nxt[j + 1] += cur[j] * p
    (cur, nxt) = (nxt, cur)
print(sum((cur[i] * i for i in range(n + 1))))
