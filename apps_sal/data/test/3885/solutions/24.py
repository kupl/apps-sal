a = int(input())
if a == 1:
    print('0')
else:
    s = 1
    t = a
    q = []
    if a % 2 == 0:
        while t > s:
            q += [s]
            q += [t]
            s += 1
            t -= 1
    else:
        while t != s:
            q += [s]
            q += [t]
            s += 1
            t -= 1
        q += [s]
    i = 0
    wyn = 0
    while i < len(q) - 1:
        wyn += (q[i] + q[i + 1]) % (a + 1)
        i += 1
    print(wyn)
