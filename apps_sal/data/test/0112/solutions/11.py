from itertools import permutations as perms


def read():
    return tuple(map(int, input().split()))


n = read()[0]
cbs = []
for i in range(n):
    cbs += [read()]
for i in range(1, 10000):
    ds = str(i)
    ch = False
    for p in perms(cbs):
        ii = []
        for k in range(len(ds)):
            for ci in range(n):
                if int(ds[k]) in p[ci] and (not ci in ii):
                    ii += [ci]
                    break
        if len(ii) == len(ds):
            ch = True
            break
    if not ch:
        print(i - 1)
        break
