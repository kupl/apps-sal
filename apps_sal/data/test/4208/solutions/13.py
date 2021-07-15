n = int(input())

l = [x for x in input()]
r = [x for x in input()]
L = {}
R = {}

for i, e in enumerate(l):
    i += 1
    if e in L:
        L[e].append(i)
    else:
        L[e] = [i]

for i, e in enumerate(r):
    i += 1
    if e in R:
        R[e].append(i)
    else:
        R[e] = [i]



res = []

q = '?'

for e in L:
    if e == q:
        continue

    if e in R:
        while len(R[e]) and len(L[e]):
            res.append((L[e].pop(), R[e].pop()))


if q in L:
    for e in R:
        if e == q:
            continue
        while L[q] and R[e]:
            res.append((L[q].pop(), R[e].pop()))

if q in R:
    for e in L:
        while L[e] and R[q]:
            res.append((L[e].pop(), R[q].pop()))


print(len(res))
for e in res:
    print(*e)

