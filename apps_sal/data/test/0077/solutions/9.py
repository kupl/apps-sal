input()
a = [int(x) for x in input().split()]
oc = 0
ps = 0
pmo = 1000000.0
nmo = -1000000.0
for x in a:
    if x > 0:
        ps += x
    if x % 2 == 1 and x > 0 and (pmo > x):
        pmo = x
    if x % 2 == 1 and x > 0:
        oc += 1
    if x % 2 == 1 and x < 0 and (nmo < x):
        nmo = x
if oc % 2 == 1:
    print(ps)
else:
    print(max(ps - pmo, ps + nmo))
