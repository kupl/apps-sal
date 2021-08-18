n = int(input())

d = {n: 0}

u = 10 ** (len(str(n)) + 2) // 9

for i in range(len(str(n)) + 1, 0, -1):

    d, e = {}, d

    u //= 10

    for v, c in list(e.items()):

        lim = v // u

        for x in range(-1 - lim, 1 - lim):

            t = v + x * u

            d[t] = min(c + i * abs(x), d.get(t, 999))

print(d[0])
