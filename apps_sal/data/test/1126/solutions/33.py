def main():
    n, x, m = map(int, input().split())
    a = [x]
    at = [x]
    aset = set(a)
    i = 1
    while(True):
        an = a[-1]**2 % m
        if an in aset:
            ca = a.index(an)
            break
        a.append(an)
        aset.add(an)
        at.append(at[-1] + a[-1])
        i += 1
        if i == n:
            print(at[-1])
            return
    ata = [0] + at[:ca]
    atb = [ata[-1]] + at[ca:]
    cb = len(atb) - 1
    na = min(n, ca)
    nb, nc = divmod(n - na, cb)
    print(ata[na] + (atb[-1] - ata[-1]) * nb + atb[nc] - ata[-1])


main()
