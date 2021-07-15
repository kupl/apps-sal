p, d = [], {}
s = 0
for i in range(int(input())):
    x, y = list(map(int, input().split()))
    for a, b in p:
        q = (a + x, b + y)
        if q not in d: d[q] = 0
        s += d[q]
        d[q] += 1
    p.append((x, y))
print(s)

