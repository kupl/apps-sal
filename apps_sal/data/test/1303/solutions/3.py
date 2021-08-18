t = list(input().split())
p = int(t[0])
q = int(t[1])
l = int(t[2])
r = int(t[3])
xv = list()
zv = list()
for i in range(p):
    t = list(int(x) for x in input().split())
    zv += list(x for x in range(t[0], t[1] + 1))
sv = set(zv)

for i in range(q):
    t = list(int(x) for x in input().split())
    xv += list(x for x in range(t[0], t[1] + 1))

c = 0
for i in range(l, r + 1):
    for j in range(q):
        tt = set((x + i) for x in xv)
        if (tt & sv) != set():
            c += 1
            break

print(c)
