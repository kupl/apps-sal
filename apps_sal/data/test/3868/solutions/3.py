def R(): return list(map(int, input().split()))


n, m, k = R()
F, T = [], []
ans = int(1e12)
for i in range(m):
    d, f, t, c = R()
    if f:
        F.append((d, f, c))
    else:
        T.append((-d, t, c))
for p in [F, T]:
    cost = [ans] * (n + 1)
    s = n * ans
    q = []
    p.sort()
    for d, t, c in p:
        if c < cost[t]:
            s += c - cost[t]
            cost[t] = c
            if s < ans:
                q.append((s, d))
    p.clear()
    p += q
s, t = ans, (0, 0)
for f in F:
    while f:
        if f[1] + t[1] + k < 0:
            s = min(s, f[0] + t[0])
        elif T:
            t = T.pop()
            continue
        f = 0
print(s if s < ans else -1)
