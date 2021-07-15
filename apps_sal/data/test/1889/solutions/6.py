a = list()
b = list()
n, m, q = [int(s) for s in input().split()]
for i in range(n):
    a.append([s for s in input().split()])
    b.append(max([len(s) for s in "".join(a[i]).split('0')]))
for i in range(q):
    p, o = [int(s)-1 for s in input().split()]
    a[p][o] = str(1-int(a[p][o]))
    b[p] = max([len(s) for s in "".join(a[p]).split('0')])
    print(max(b))

