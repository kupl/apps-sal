h, m, s, a, b = list(map(int, input().split()))

m += s / 60
h += m / 60
m /= 5
s /= 5


c = [h, m, s, a, b]
c = c + list([x + 12 for x in c])
c = sorted(c)
p = c.index(a)
for x in [p - 1, p + 1]:
    for y in [b, b + 12]:
        if c[x] == y:
            print('YES')
            return

print('NO')
