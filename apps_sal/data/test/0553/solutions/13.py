import math


def fnd(a, m, key):  # next
    f1 = [0, 1][key]
    f2 = [lambda m:math.floor(m), lambda m:math.ceil(m)][key]
    if type(m) == int:
        return -1
    if m[0] > a:
        return -1
    if m[-1] < a:
        return -1
    if len(m) == 2:
        return(m[f1])

    r = list([m for m in [fnd(a, m[len(m) // 2:], key), fnd(a, m[:len(m) // 2 + 1], key)] if m != -1])
    if len(r) == 0:
        return m[f2(len(m) / 2)]
    return r[0]


def F(a, m, key=True):
    if (m[0] > a) and key: return m[0]
    if (m[-1] < a) and not key: return m[-1]
    return fnd(a, m, key)


def distance(a, b):
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
    return c


n = int(input())
promos = []
for i in range(n):
    promos += [input()]
if len(promos) == 1:
    print(6)
    return
#print([(x,y) for x in promos for y in promos if x!=y])
a = min([distance(promos[x], promos[y]) for x in range(len(promos)) for y in range(x + 1, len(promos))])
r = [x for x in range(a + 1) if x != a / 2]
print(F(a / 2, r, False))
