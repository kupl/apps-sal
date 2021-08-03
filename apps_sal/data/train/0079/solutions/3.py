import itertools
def y(): return int(input())


p = [1] * 32000
for i in range(180):
    if p[i]:
        for j in range(2 * i + 2, len(p), i + 2):
            p[j] = 0
q = [i + 2 for i in range(len(p))if p[i]]
for _ in range(y()):
    n = y()
    d = []
    e = set()
    for i in q:
        if n % i < 1:
            n //= i
            d.append([i, 1])
            while n % i < 1:
                n //= i
                d[-1][1] += 1
    if n > 1:
        d.append([n, 1])
    l = len(d)
    for i in itertools.product(*(range(i[1] + 1)for i in d)):
        p = 1
        for j in range(l):
            p *= d[j][0]**i[j]
        e.add(p)
    e.remove(1)

    b = l == 2 and d[0][1] + d[1][1] == 2
    if l < 2 or b:
        f = list(e)
    elif l < 3:
        s = d[1][1] > 1
        v = d[s][0] * d[1 - s][0]
        f = [v]
        e.remove(v)
        k = set()
        for i in e:
            if i % d[1 - s][0] < 1:
                k.add(i)
                f.append(i)
        v = (d[s][0]**2) * d[1 - s][0]
        f.remove(v)
        f.append(v)
        e -= k
        for i in e:
            f.append(i)
    else:
        v = d[0][0] * d[-1][0]
        f = [v]
        e.remove(v)
        for i in range(l):
            v = d[i][0] * d[i - 1][0]
            f.remove(v)
            f.append(v)
            k = set()
            for j in e:
                if j % d[i][0] < 1:
                    k.add(j)
                    f.append(j)
            e -= k
    print(' '.join(map(str, f)))
    print(int(b))
