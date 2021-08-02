def unique(a):
    if len(a) == 0:
        return a

    i = 1
    j = 1
    last = a[0]
    while j < len(a):
        if a[j] > last:
            last = a[j]
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1

    return a[:i]


def expand(cir):
    e = []
    for i in range(len(cir)):
        e.append(cir[i][0])
    for i in range(-1, -len(cir) - 1, -1):
        for _ in range(cir[i][1] - 1):
            e.append(cir[i][0])

    return e


n = int(input())
a = list(map(int, input().split(' ')))

c = dict()
for x in a:
    if x in c:
        c[x] += 1
    else:
        c[x] = 1

a.sort()
a = unique(a)
n = len(a)

cir = []
cirsize = 0

i = 0
while i < n:
    j = i + 1
    while j < n and a[j] == a[j - 1] + 1 and c[a[j]] > 1:
        j += 1
    if j < n and a[j] == a[j - 1] + 1:
        j += 1

    sz = 0
    for p in range(i, j):
        sz += c[a[p]]
    if sz > cirsize:
        cir.clear()
        for p in range(i, j):
            cir.append((a[p], c[a[p]]))
        cirsize = sz

    if c[a[j - 1]] == 1 and i != j - 1:
        i = j - 1
    else:
        i = j

print(cirsize)
print(*expand(cir))
