(n, m) = [int(el) for el in input().split()]
pair = []
kol = {i: 1 for i in range(1, n + 1)}
for i in range(m):
    (q, w) = [int(el) for el in input().split()]
    if q < w:
        pair.append((q, w))
    else:
        (q, w) = (w, q)
        pair.append((q, w))
    kol[q] += 1
    kol[w] += 1
pair.sort()
mazy = []
for i in range(1, n + 1):
    mazy.append((i, i, i))
for i in pair:
    mazy.append((i[0], 10000 * i[1] + i[0], i[0]))
    mazy.append((i[1], 10000 * i[1] + i[0], i[1]))
mazy.sort()
cur = 1
print(kol[1])
while mazy != []:
    q = mazy.pop(0)
    if q[0] == cur:
        print(q[1], q[0])
    else:
        print(kol[q[0]])
        print(q[1], q[0])
        cur = q[0]
