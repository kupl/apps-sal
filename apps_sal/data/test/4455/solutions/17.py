from copy import copy

n, k = map(int, input().split(' '))
l = list(map(int, input().split(' ')))
r = copy(l)

idd = dict()
for i in range(n):
    try:
        idd[l[i]].add(i)
    except:
        idd[l[i]] = {i}

nd = dict()
l.sort()

used = set()

for i in enumerate(l):
    if not i[1] in used:
        for x in idd[i[1]]:
            nd[x] = i[0]
        used.add(i[1])

d = {i: 0 for i in range(n)}

for i in range(k):
    a, b = map(lambda x: int(x) - 1, input().split(' '))
    if r[a] < r[b]:
        d[b] += 1
    elif r[b] < r[a]:
        d[a] += 1

for i in range(n):
    print(nd[i] - d[i], end=' ')
