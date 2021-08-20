q = int(input())
dz = [set() for i in range(13337)]
dz[1].add(1)
dz[2].add(1)
dz[2].add(2)
for k in range(3, 13337):
    i = 2
    cyk = 0
    while i ** 2 <= k:
        if k % i == 0:
            cyk = 1
            break
        i += 1
    if cyk == 0:
        dz[k].add(1)
        dz[k].add(k)
    else:
        kk = k
        dzi = 1
        while kk % i == 0:
            dzi *= i
            kk //= i
        pom = dz[kk]
        dupa = set()
        for j in pom:
            dupa.add(j * dzi)
        dz[k] = dz[k // i].union(dupa)
for _ in range(q):
    (a, b, c) = map(int, input().split())
    bestie = [a, b, c]
    best = 34739174893

    def wyn(x, y, z):
        return abs(x - a) + abs(y - b) + abs(z - c)
    for z in range(1, 13337):
        if abs(z - c) > best:
            continue
        for y in dz[z]:
            if abs(z - c) + abs(y - b) > best:
                continue
            for x in dz[y]:
                if wyn(x, y, z) < best:
                    bestie = [x, y, z]
                    best = wyn(x, y, z)
    print(best)
    print(*bestie)
