a = [int(s) for s in input().split()]
g = {i: [] for i in range(1, a[0] + 1)}
for i in range(a[1]):
    c = [int(s) for s in input().split()]
    g[c[0]].append(c[1])
    g[c[1]].append(c[0])
j = 0
d = {i: False for i in range(1, a[0] + 1)}
for i in range(1, a[0] + 1):
    if d[i] == False:
        j += 1
        d[i] = True
        if g[i] != []:
            Q = [i]
            while Q != []:
                r = Q.pop(0)
                if g[r] != []:
                    for m in g[r]:
                        if d[m] == False:
                            d[m] = True
                            Q.append(m)
print(j)
