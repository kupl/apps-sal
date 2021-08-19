n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [0] * n
d = set([x for x in range(1, n + 1)])
for x in range(n):
    if a[x] == b[x]:
        c[x] = a[x]
        d.remove(a[x])
    elif a.count(a[x]) + b.count(a[x]) == 1:
        c[x] = a[x]
        d.remove(a[x])
    elif a.count(b[x]) + b.count(b[x]) == 1:
        c[x] = b[x]
        d.remove(b[x])
if len(d) == 0:
    ty = str(c)[1:-1].replace(',', '')
    print(ty)
if len(d) == 1:
    c[c.index(0)] = d.pop()
    ty = str(c)[1:-1].replace(',', '')
    print(ty)
elif len(d) == 2:
    c[c.index(0)] = d.pop()
    c[c.index(0)] = d.pop()
    ty = str(c)[1:-1].replace(',', '')
    print(ty)
