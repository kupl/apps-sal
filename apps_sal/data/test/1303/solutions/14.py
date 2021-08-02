p, q, l, r = list(map(int, input().split(' ')))
plist = list()
qlist = list()
for i in range(p):
    plist.append(list(map(int, input().split())))
for i in range(q):
    qlist.append(list(map(int, input().split())))

pset = set()
qset = set()
for j in range(p):
    pset = pset | set(range(plist[j][0], plist[j][1] + 1))

whengetup = 0
for i in range(l, r + 1):
    qset = set()
    for j in range(q):
        qset = qset | set(range(qlist[j][0] + i, qlist[j][1] + i + 1))
    if len(pset & qset) > 0:
        whengetup += 1

print(whengetup)
