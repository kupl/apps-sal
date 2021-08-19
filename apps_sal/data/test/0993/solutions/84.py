(n, m, *c) = map(int, open(0).read().split())
d = {0: 1}
r = s = 0
for i in c:
    s += i
    s %= m
    x = d.get(s, 0)
    r += x
    d[s] = x + 1
print(r)
