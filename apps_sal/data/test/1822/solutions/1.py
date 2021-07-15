

n, x = list(map(int, input().split()))

a = [-10000] + list(map(int, input().split()))

ceps = []
ones = 0
was = set()

for i in range(1, n+1):
    if i not in was and i not in a:
        cep = [i]
        while a[i]:
            cep.append(a[i])
            i = a[i]
        for i in cep:
            was.add(i)
        #print(cep)
        if x in cep:
            r = cep.index(x)
            l = len(cep) - r - 1
        else:
            if len(cep) == 1:
                ones += 1
            else:
                ceps.append(len(cep))

import itertools

sums = set(ceps)
for i in range(2, len(ceps)+1):
    for comb in itertools.combinations(ceps, i):
        sums.add(sum(comb))
sums.add(0)

poss = set()
#print(l + 1)
for s in sums:
    for i in range(ones+1):
        poss.add(l + s + 1 + i)
    #print(l + s + 1)

for pos in sorted(poss):
    print(pos)

