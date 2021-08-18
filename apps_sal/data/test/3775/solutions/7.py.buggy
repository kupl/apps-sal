n, m = list(map(int, input().split()))
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

a = []
b = []

for i in range(0, 2 * n, 2):
    a.append([aa[i], aa[i + 1]])

for i in range(0, 2 * m, 2):
    b.append([bb[i], bb[i + 1]])

accept = []

for num in range(1, 10):
    ina = []
    inb = []
    for x in a:
        if num in x:
            ina.append(x)

    for x in b:
        if num in x:
            inb.append(x)

    x = 0
    for t in ina:
        t.sort()
        for p in inb:
            p.sort()
            if t != p:
                x += 1
    if x > 0:
        accept.append(num)

if len(accept) == 1:
    print(accept[0])
    return

# check fst
for t in a:
    z = set()
    for p in b:
        if t != p:
            if t[0] in p:
                z.add(t[0])
            if t[1] in p:
                z.add(t[1])
    if len(z) > 1:
        print(-1)
        return

# check scd
for t in b:
    z = set()
    for p in a:
        if t != p:
            if t[0] in p:
                z.add(t[0])
            if t[1] in p:
                z.add(t[1])
    if len(z) > 1:
        print(-1)
        return
print(0)
