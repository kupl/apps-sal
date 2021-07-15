x = input()
y = input()

g1 = {}
g2 = {}
g3 = {}
g4 = {}

for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    g2[i] = 0
    g4[i] = 0

for i in 'abcdefghijklmnopqrstuvwxyz':
    g1[i] = 0
    g3[i] = 0
    
e = 0
f = 0

u = []
l = []
u2 = []
l2 = []
for i in x:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        u.append(i)
        g2[i] += 1
    else:
        l.append(i)
        g1[i] += 1
        
for i in y:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        u2.append(i)
        g4[i] += 1
    else:
        l2.append(i)
        g3[i] += 1

for i in g1:
    ct = g1[i]
    can = g3[i]
    if ct != 0 and can != 0:
        if ct > can:
            g1[i] = ct - can
            g3[i] = 0
            e += can
        else:
            g3[i] = can - ct
            e += g1[i]
            g1[i] = 0
            

for i in g2:
    ct = g2[i]
    can = g4[i]
    if ct != 0 and can != 0:
        if ct > can:
            g2[i] = ct - can
            g4[i] = 0
            e += can
        else:
            g4[i] = can - ct
            e += g2[i]
            g2[i] = 0

for i in g1:
    ct = g1[i]
    can = g4[i.upper()]
    if ct != 0 and can != 0:
        if ct > can:
            g1[i] = ct - can
            g4[i.upper()] = 0
            f += can
        else:
            g4[i.upper()] = can - ct
            f += g1[i]
            g1[i] = 0
            

for i in g2:
    ct = g2[i]
    can = g3[i.lower()]
    if ct != 0 and can != 0:
        if ct > can:
            g2[i] = ct - can
            g3[i.lower()] = 0
            f += can
        else:
            g3[i.lower()] = can - ct
            f += g2[i]
            g2[i] = 0
            

print(e, f)

