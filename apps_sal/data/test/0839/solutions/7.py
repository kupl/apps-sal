def str(l, l1, l2, l3, l4):
    s = [l, l1, l2, l3, l4]
    return s
def count(u):
    sum = 0
    lim = 0
    while lim != 5:
        for i in range(0, len(u) - 1, 2):
            sum += a[u[i]-1][u[i+1]-1]
            sum += a[u[i+1]-1][u[i]-1]
        u = u[1:]
        lim += 1
    return sum
a = []
u = [1, 2, 3, 4 ,5]
for i in range(5):
    a.append(list(map(int, input().split())))
b = []
c = []
o = set()
for i in range(1, 6):
    for j in range(1, 6):
        for k in range(1, 6):
            for l in range(1, 6):
                for p in range(1, 6):
                    o.add(i)
                    o.add(j)
                    o.add(k)
                    o.add(l)
                    o.add(p)
                    if len(o) == 5:
                        b.append(str(i, j, k, l, p))
                    o = set()
for i in range(len(b)):
    c.append(count(b[i]))
c = sorted(c)
print(c[-1])
