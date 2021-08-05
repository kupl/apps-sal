n = int(input())
a = [int(x) for x in input().split()]
dtt = dict()
for t in a:
    if t in dtt:
        dtt[t] += 1
    else:
        dtt[t] = 1
lts = [dtt[x] for x in dtt]
lts.sort(reverse=True)
mt = [lts[0]]
pl = lts[0]
for d in range(1, len(lts)):
    cl = min(pl // 2, lts[d])
    if cl == 0:
        break
    cs = cl * (2**(d + 1) - 1)
    mt.append(cs)
    pl = cl
print(max(mt))
