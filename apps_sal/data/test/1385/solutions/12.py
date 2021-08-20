l = input().strip()
r = []
u = l.split('"')
if l[-1] == '"':
    u.pop()
v = len(u)
for i in range(v):
    if i % 2:
        r.append(u[i])
    else:
        x = u[i].split()
        for j in x:
            r.append(j)
for u in r:
    print('<', u, '>', sep='')
