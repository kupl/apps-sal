R = input
(n, m) = map(int, R().split())
N = range(n)
v = zip(*map(list, [R() for _ in N]))
g = [0] * n
s = 0
for r in v:
    if sum((g[i] or r[i] >= r[i - 1] for i in N[1:])) < n - 1:
        s += 1
    else:
        for i in N[1:]:
            g[i] |= r[i] > r[i - 1]
print(s)
