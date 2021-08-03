def read():
    return [int(x) for x in input().split()]


k, n = read()
a = read()
b = read()

c = []
for x in a:
    c.append((c[-1] if c else 0) + x)
c = set(c)

z = set()

s = 0
for x in a:
    s += x
    i = b[0] - s
    for y in b[1:]:
        if y - i not in c:
            break
    else:
        z.add(i)

print(len(z))
