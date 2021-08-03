from functools import reduce
import operator

t = int(input())
for _ in range(t):
    n = int(input())
    ds = sorted(map(int, input().split()))
    suspect = ds[0] * ds[-1]
    pfs = []
    g = suspect
    for i in range(2, int(g**0.5) + 1):
        if g % i == 0:
            pfs.append([0, i])
            while g % i == 0:
                pfs[-1][0] += 1
                g //= i
    if 1 < g:
        pfs.append([1, g])
    nf = reduce(operator.mul, [u[0] + 1 for u in pfs])
    ok = nf == len(ds) + 2
    for d in ds:
        if suspect % d != 0:
            ok = False
    if ok:
        print(suspect)
    else:
        print(-1)
