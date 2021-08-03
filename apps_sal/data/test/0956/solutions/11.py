m, k1 = map(int, input().split())
d = dict()
s = set()


for i in range(m):
    a, b = map(int, input().split())
    s.add(a)
    s.add(b)
    if a in d:
        d[a].add(b)
    else:
        d[a] = set()
        d[a].add(b)

    if b in d:
        d[b].add(a)
    else:
        d[b] = set()
        d[b].add(a)
ar = []
for i in s:
    ar.append(i)
ar = list(sorted(ar))
for i in ar:
    print(str(i) + ": ", end='')
    sumfr = 0
    arfr = []
    for j in ar:
        if j != i and not(j in d[i]):
            sum1 = 0
            sumall = 0
            for k in d[i]:
                if j in d[k] and j != k:
                    sum1 += 1
            pr = sum1 / len(d[i]) * 100

            if pr >= k1 - 0.000001:
                sumfr += 1
                arfr.append(j)

    print(sumfr, end=' ')
    for i in arfr:
        print(i, end=' ')
    print()
