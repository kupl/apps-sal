n = int(input())
p = {}
o = {}
for i in range(n):
    e = input().split()
    if not e[0] in p:
        p[e[0]] = []
    for x in e[2:]:
        p[e[0]].append((len(x), x[::-1]))
for i in p:
    for x in sorted(p[i])[::-1]:
        f = False
        if not i in o:
            o[i] = []
        for z in o[i]:
            f |= x[1]==z or (x[0]<len(z) and x[1]==z[:x[0]])
        if not f:
            o[i].append(x[1])
print(len(o))
for i in o:
    print(i + ' ' + str(len(o[i])) + ' ' + ' '.join(x[::-1] for x in o[i]))

