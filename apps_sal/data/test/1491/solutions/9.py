n = int(input())
s = 0
kolzero = 0
l = [int(i) for i in input().split()]
kv = 0
for i in range(n):
    if int(l[i] ** 0.5) ** 2 == l[i]:
        kv += 1
g = [0] * n
for i in range(n):
    if l[i] == 0:
        kolzero += 1
    a = int(l[i] ** 0.5)
    b = a + 1
    a = a ** 2
    b = b ** 2
    if l[i] - a < b - l[i]:
        g[i] = l[i] - a
    else:
        g[i] = b - l[i]
i = 0
x = 0
if kv >= n // 2:
    s = kv - n // 2
    if kolzero > n // 2:
        s += kolzero - n // 2
    print(s)
else:
    g.sort()
    while x < n // 2 - kv:
        if g[i] != 0:
            s += g[i]
            x += 1
        i += 1
    print(s)
