from math import ceil

t = int(input())
for _ in range(t):
    n = int(input())
    pf = []
    for i in range(2, ceil(n**0.5) + 1):
        while n % i == 0:
            pf.append(i)
            n //= i
    if n > 1:
        pf.append(n)
    if len(pf) == 2 and pf[0] != pf[1]:
        print(pf[0], pf[1], pf[0] * pf[1])
        print(1)
    else:
        pg = []
        fac = []
        nfac = []
        while len(pf) > 0:
            p = pf[-1]
            mul = 0
            while len(pf) > 0 and pf[-1] == p:
                pf.pop()
                mul += 1
            pg.append([mul, p])
        pg.sort()
        pg = pg[::-1]
        # print(pg)
        cur = 0
        if pg[0][0] == 1:
            a = pg[0][1]
            b = pg[1][1]
            c = pg[2][1]
            fac = [a, a * b * c, a * b, b, b * c, c, a * c]
            cur = 3
        else:
            fac = [pg[0][1]**i for i in range(1, pg[0][0] + 1)]
            cur = 1
        while cur < len(pg):
            mul = pg[cur][0]
            p = pg[cur][1]
            nfac = []
            for i in range(len(fac)):
                if i == 0:
                    nfac += [fac[i] * (p**j) for j in range(mul, -1, -1)]
                else:
                    nfac += [fac[i] * (p**j) for j in range(mul + 1)]
            nfac += [p**i for i in range(1, mul + 1)]
            fac = nfac
            cur += 1
        print(" ".join([str(i) for i in fac]))
        print(0)
