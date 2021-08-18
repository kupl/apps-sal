n, k = list(map(int, input().split()))
days = list(map(int, input().split()))
a = [0 for i in range(n)]
b = [0 for i in range(n)]
asum = 0
ia = 0
ib = 0
inf = n + 199

for x in days:
    if x < 0:
        a[ia] += 1
        asum += 1
        if b[ib] != 0:
            ib += 1
    else:
        b[ib] += 1
        if a[ia] != 0:
            ia += 1
changes = ia + 1 if a[ia] > 0 else ia
changes += changes - 1
if (a[ia] == 0):
    ia -= 1
if b[ib] == 0:
    ib -= 1
if asum > k:
    print(-1)
    quit()
for i in range(ia, n):
    a[i] = inf if a[i] == 0 else a[i]
for i in range(ib, n):
    b[i] = inf if b[i] == 0 else b[i]
if days[0] >= 0:
    b[0] = inf
lastb = -1
removedlastb = False
if days[len(days) - 1] >= 0:
    changes += 1
    lastb = b[ib]
b.sort()
curb = 0
seccurb = curb
secasum = asum
secchanges = changes
secremovedlastb = removedlastb
while (curb <= ib and asum + b[curb] <= k):
    asum += b[curb]
    if not removedlastb:
        if b[curb] == lastb:
            changes -= 1
            removedlastb = True
        else:
            changes -= 2
    else:
        changes -= 2
    curb += 1
while (seccurb <= ib and secasum + b[seccurb] <= k):
    secasum += b[seccurb]
    if not secremovedlastb:
        if b[seccurb] == lastb:
            secasum -= b[seccurb]
            secremovedlastb = True
        else:
            secchanges -= 2
    else:
        secchanges -= 2
    seccurb += 1
print(max(min(changes, secchanges), 0))
