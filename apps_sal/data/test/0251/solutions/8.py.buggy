n, k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
mih = min(h)
mah = max(h)
if mah == mih:
    print(0)
    return
cotam = dict()
lotam = list()
sotam = set()
for th in h:
    if th > mih:
        if th in sotam:
            cotam[th] += 1
        else:
            sotam.add(th)
            lotam.append(th)
            cotam[th] = 1
lotam.sort(reverse=True)

sc = 0
cc = 0
rk = 0
for i in range(len(lotam)):
    ch = lotam[i]
    nh = (mih if i >= len(lotam) - 1 else lotam[i + 1])
    cc += cotam[ch]
    if rk >= cc:
        hrbrk = min(ch - nh, rk // cc)
        rk -= cc * hrbrk
        ch -= hrbrk
    while ch > nh:
        hrbk = min(ch - nh, k // cc)
        sc += 1
        ch -= hrbk
        rk = k - hrbk * cc
print(sc)
