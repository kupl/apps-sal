DBG = False
(n, q) = list(map(int, input().split()))
l = []
r = []
c = [0] * (n + 2)
for i in range(q):
    (ll, rr) = list(map(int, input().split()))
    l.append(ll)
    r.append(rr)
    for j in range(ll, rr + 1):
        c[j] += 1
acc1 = [0] * (n + 2)
acc12 = [0] * (n + 2)
for j in range(1, n + 1):
    acc1[j] = acc1[j - 1] + (1 if c[j] == 1 else 0)
    acc12[j] = acc12[j - 1] + (1 if c[j] == 2 else 0)
minred = 99999999
for i in range(q - 1):
    for j in range(i + 1, q):
        li = l[i]
        lj = l[j]
        ri = r[i]
        rj = r[j]
        if li > lj:
            (li, lj) = (lj, li)
            (ri, rj) = (rj, ri)
        if rj <= ri:
            oneal = li
            onear = lj - 1
            twol = lj
            twor = rj
            onebl = rj + 1
            onebr = ri
        elif lj <= ri:
            oneal = li
            onear = lj - 1
            twol = lj
            twor = ri
            onebl = ri + 1
            onebr = rj
        else:
            oneal = li
            onear = ri
            twol = lj
            twor = lj - 1
            onebl = lj
            onebr = rj
        onereda = acc1[onear] - acc1[oneal - 1]
        oneredb = acc1[onebr] - acc1[onebl - 1]
        twored = acc12[twor] - acc12[twol - 1]
        redsum = onereda + oneredb + twored
        minred = min(minred, redsum)
zcnt = 0
for i in range(1, n + 1):
    if c[i] == 0:
        zcnt += 1
print(n - zcnt - minred)
