from collections import deque
n = int(input())
l = input()
r = input()
a = [0 for i in range(0, ord('z') + 1)]
b = [0 for i in range(0, ord('z') + 1)]
c = [deque() for i in range(0, ord('z') + 1)]
d = [deque() for i in range(0, ord('z') + 1)]
for i in range(len(l)):
    if l[i] == '?':
        a[0] += 1
        c[0].append(i + 1)
    else:
        a[ord(l[i])] += 1
        c[ord(l[i])].append(i + 1)
for i in range(len(l)):
    if r[i] == '?':
        b[0] += 1
        d[0].append(i + 1)
    else:
        b[ord(r[i])] += 1
        d[ord(r[i])].append(i + 1)
vopra = a[0]
voprb = b[0]
sch = 0
out = []
for i in range(1, len(a)):
    sch += min(a[i], b[i])
    sch += min(voprb, a[i] - min(a[i], b[i]))
    for j in range(min(a[i], b[i])):
        if min(a[i], b[i]) > 0:
            out.append([c[i].popleft(), d[i].popleft()])
    for j in range(min(voprb, a[i] - min(a[i], b[i]))):
        if min(voprb, a[i] - min(a[i], b[i])) > 0:
            out.append([c[i].popleft(), d[0].popleft()])
    voprb -= min(voprb, a[i] - min(a[i], b[i]))
    sch += min(vopra, b[i] - min(a[i], b[i]))
    for j in range(min(vopra, b[i] - min(a[i], b[i]))):
        if min(vopra, b[i] - min(a[i], b[i])) > 0:
            out.append([c[0].popleft(), d[i].popleft()])
    vopra -= min(vopra, b[i] - min(a[i], b[i]))
if vopra > 0 and voprb > 0:
    sch += min(vopra, voprb)
    for j in range(min(vopra, voprb)):
        if min(vopra, voprb) > 0:
            out.append([c[0].popleft(), d[0].popleft()])
print(sch)
for i in out:
    print(*i)
