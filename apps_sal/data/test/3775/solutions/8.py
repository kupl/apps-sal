iter = 0
n, m = list(map(int, input().split()))
temppair = [0, 0]
i1 = list(map(int, input().split()))
i2 = list(map(int, input().split()))
l1 = []
l2 = []
d = 0
for i in i1:
    if(d == 0):
        temppair[0] = i
        d = 1
    else:
        temppair[1] = i
        d = 0
        l1.append(sorted(temppair.copy()))
for i in i2:
    if(d == 0):
        temppair[0] = i
        d = 1
    else:
        temppair[1] = i
        d = 0
        l2.append(sorted(temppair.copy()))
dic1 = dict()
dic2 = dict()
for i in range(len(l1)):
    l1[i] = (iter, l1[i])
    iter += 1
for i in range(len(l2)):
    l2[i] = (iter, l2[i])
    iter += 1
for e in l1:
    for e1 in l2:
        if(((e[1][0] in e1[1]) or (e[1][1] in e1[1])) and e[1] != e1[1]):
            dic1[e[0]] = dic1.get(e[0], []) + [e1[1]]
for e in l2:
    for e1 in l1:
        if(((e[1][0] in e1[1]) or (e[1][1] in e1[1])) and e[1] != e1[1]):
            dic2[e[0]] = dic2.get(e[0], []) + [e1[1]]
mybool = True
for k, v in list(dic1.items()):
    k = l1[k][1]
    mybool = mybool and (all([k[0] in p for p in v]) or all([k[1] in p for p in v]))
for k, v in list(dic2.items()):
    k = k - len(l1)
    k = l2[k][1]
    mybool = mybool and (all([k[0] in p for p in v]) or all([k[1] in p for p in v]))

c1 = True
dk1 = list(dic1)
dk1 = list([l1[k][1] for k in dk1])
sameone = dk1[0][0]
c1 = all([sameone in u for u in dk1])
for v in list(dic1.values()):
    c1 = c1 and all([sameone in u for u in v])

if not c1:
    c1 = True
    sameone = dk1[0][1]
    c1 = all([sameone in u for u in dk1])
    for v in list(dic1.values()):
        c1 = c1 and all([sameone in u for u in v])


if(c1):
    e, e1 = list(dic1.items())[0]
    e = l1[e][1]
    e1 = e1[0]
    if (e[0] in e1):
        print(e[0])
        quit()
    else:
        print(e[1])
        quit()
elif(mybool):
    print(0)
    quit()
else:
    print(-1)
