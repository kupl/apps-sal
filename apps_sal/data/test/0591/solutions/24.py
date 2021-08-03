def f(idl, idr, x):
    if idr - idl < 2:
        return
    m = (idr + idl) // 2
    i = idl
    j = m
    f(idl, m, x)
    f(m, idr, x)
    a = []
    for k in range(idr - idl):
        if j >= idr or (i < m and x[i] < x[j]):
            a.append(x[i])
            i += 1
        else:
            a.append(x[j])
            j += 1
    for k in range(idr - idl):
        x[k + idl] = a[k]


fi = open('input.txt', 'r')
n, k = map(int, fi.readline().split())
a = fi.readline().split()
a = [[int(a[x]), x + 1] for x in range(n)]
f(0, n, a)
fo = open('output.txt', 'w')
print(a[-k][0], file=fo)
print(*[x[1] for x in a[-k:]], file=fo)
