s = input()
if int(s) % 25 == 0:
    print(0)
else:
    sols = []
    d = {}
    n = list(s)
    nr = s[::-1]
    for c in ('0', '2', '5', '7'):
        p = nr.find(c)
        d[c] = p
    for (c1, c2) in (('2', '5'), ('5', '0'), ('7', '5')):
        if c1 not in n or c2 not in n:
            continue
        dc1 = d[c1]
        dc2 = d[c2]
        sol = 0
        if dc1 == len(n) - 1 and len(n) > 1 and (n[1] == '0'):
            i = 1
            while i < len(n) and (n[i] == '0' or dc2 == i):
                i += 1
            if i != len(n):
                i -= 1
                sol = i
                dc1 -= 1
                if dc2 > len(n) - i - 1:
                    dc2 -= 1
        if dc2 == len(n) - 1 and len(n) > 1 and (n[1] == '0'):
            i = 1
            while i < len(n) and (n[i] == '0' or dc1 == i):
                i += 1
            if i != len(n):
                sol = i
                dc2 -= 1
                if dc1 > len(n) - i - 1:
                    dc1 -= 1
        if dc1 == 0:
            sols.append(dc2 + sol)
            continue
        if dc1 < dc2:
            sols.append(dc2 + dc1 + sol)
        else:
            sols.append(dc2 + dc1 - 1 + sol)
    z1 = nr.find('0')
    if z1 != -1:
        z2 = nr.find('0', z1 + 1)
        if z2 != -1:
            sols.append(z1 + z2 - 1)
    if len(sols) == 0:
        print(-1)
    else:
        print(min(sols))
