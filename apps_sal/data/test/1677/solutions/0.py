(d, n, t) = (0, int(input()), list(map(int, input().split())))
p = {a: 0 for a in set(t)}
for i in range(n):
    a = t[i]
    if not a in p:
        continue
    p.pop(a)
    s = t.count(a) - 1
    if 2 * s < d:
        continue
    if s > d:
        d = s
    k = i + 1
    for j in range(k, n):
        if t[j] == a:
            for b in set(t[k:j]):
                if b in p:
                    p[b] += 2
            k = j + 1
    for b in set(t[k:n]):
        if b in p:
            p[b] += 1
    for b in p:
        if p[b] > d:
            d = p[b]
        p[b] = 0
print(d + 1)
