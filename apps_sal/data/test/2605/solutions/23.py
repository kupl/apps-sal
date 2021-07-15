n, k = map(int, input().split())
c = list(map(int, input().split()))
v = c[0] * c[n - 1] + sum(c[i] * c[i + 1] for i in range(n - 1))
s, ss, cs = set(), 0, sum(c)
for k in map(int, input().split()):
    a, b, x = n if k == 1 else k - 1, 1 if k == n else k + 1, 0
    if a not in s:
        x += c[a - 1]
    if b not in s:
        x += c[b - 1]
    v += c[k - 1] * (cs - c[k - 1] - ss - x)
    s.add(k)
    ss += c[k - 1]
print(v)
