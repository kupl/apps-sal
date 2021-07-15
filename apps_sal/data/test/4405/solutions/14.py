n = int(input())
a = [int(i) for i in input().split()]

dtt = dict()

for v in a:
    if v not in dtt:
        dtt[v] = 0
    dtt[v] += 1

lts = [dtt[i] for i in dtt]
lts.sort(reverse=True)

mt = [lts[0]]
pl = lts[0]

for i in range(1,len(lts)):
    cl = min(pl//2,lts[i])
    if cl == 0:
        break
    cs = cl*(2**(i+1)-1)
    mt.append(cs)
    pl = cl

print(max(mt))

