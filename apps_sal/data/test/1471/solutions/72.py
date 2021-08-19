g = {}
a = int(input())
for i in range(a - 1):
    c = [int(s) for s in input().split()]
    if c[0] not in g:
        g[c[0]] = [(c[1], c[2])]
    else:
        g[c[0]].append((c[1], c[2]))
    if c[1] not in g:
        g[c[1]] = [(c[0], c[2])]
    else:
        g[c[1]].append((c[0], c[2]))
c = {}
d = {i: False for i in range(1, a + 1)}
(c[1], d[1]) = (0, True)
Q = [1]
while Q != []:
    r = Q.pop(0)
    for i in g[r]:
        if d[i[0]] == False:
            d[i[0]] = True
            Q.append(i[0])
            if i[1] % 2 == 0:
                c[i[0]] = c[r]
            else:
                c[i[0]] = (c[r] + 1) % 2
for i in range(1, a + 1):
    print(c[i])
