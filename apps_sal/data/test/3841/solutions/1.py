[p, k] = [int(x) for x in input().split()]
d = 1
res = []
while p:
    if d % 2 == 1:
        kek = k
        res.append(str(p % kek))
        p //= kek
    else:
        kek = k
        lol = kek - p % kek
        while lol >= kek:
            lol -= kek
        res.append(str(lol))
        p = (p + lol) // kek
    d += 1
print(len(res))
s = ' '
print(s.join(res))
