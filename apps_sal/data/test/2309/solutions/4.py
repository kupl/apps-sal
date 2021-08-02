voy = ['a', 'e', 'i', 'o', 'u']


def de(a):
    for i in a[::-1]:
        if i in voy:
            return i


di = {}
ta = set()
for k in range(int(input())):
    a = input()
    nb = sum((i in voy) for i in a)
    if not(nb in ta):
        for v in voy:
            di[(nb, v)] = []
        ta.add(nb)
    d = de(a)
    cl = (nb, d)
    di[cl].append(a)
co1 = sum(len(di[k]) // 2 for k in di)
co2 = sum(sum(len(di[k, v]) for v in voy) // 2 for k in ta) // 2
wo = []
co = min(co1, co2)
nb = 0
for k in di:
    nbl = 0
    for i, j in zip(di[k][::2], di[k][1::2]):
        if nb != co:
            wo.append([i, j])
            nb += 1
            nbl += 1
    di[k] = di[k][2 * nbl:]
di2 = [di[k, 'a'] + di[k, 'e'] + di[k, 'i'] + di[k, 'o'] + di[k, 'u'] for k in ta]
p = 0
for k in di2:
    for i, j in zip(k[::2], k[1::2]):
        if p != len(wo):
            wo[p].append(i)
            wo[p].append(j)
            p += 1
print(co)
for k in wo:
    print(k[2], k[0])
    print(k[3], k[1])
