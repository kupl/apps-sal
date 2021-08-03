m, k = map(int, input().split())
fr = []
ppl = set()
for i in range(m):
    a, b = map(int, input().split())
    fr.append((a, b))
    ppl.add(a)
    ppl.add(b)
pairs = {}
for i in ppl:
    pairs[i] = set()
for i in fr:
    pairs[i[0]].add(i[1])
    pairs[i[1]].add(i[0])
# print (pairs)
for i in sorted(ppl):
    tmp = []
    pi = pairs[i]
    qwe = len(pi) * k
    for j in ppl:
        if j in pi or i == j:
            continue
        if len(pi.intersection(pairs[j])) * 100 >= qwe:
            tmp.append(j)
    print("%d: %d %s" % (i, len(tmp), ' '.join(map(str, sorted(tmp)))))
