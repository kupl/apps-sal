m, k = map(int, input().split())
a = list()
s = set()
for i in range(m):
    c = list(map(int, input().split()))
    a.append(c)
    s.add(c[0])
    s.add(c[1])
d = dict()
for i in s:
    d[i] = set()
for i in a:
    d[i[0]].add(i[1])
    d[i[1]].add(i[0])

tmp = list()
sor = list(s)
sor.sort()
for i in sor:
    tmp = list()
    for j in sor:
        if (i != j) & (j not in d[i]):
            m = d[i] & d[j]
#			print(i, j, d[i] & d[j])
            if (len(m) / len(d[i])) - (k / 100.0) > -0.000000001:
                tmp.append(j)
    print(i, ": ", len(tmp), " ", " ".join(map(str, tmp)), sep="")
