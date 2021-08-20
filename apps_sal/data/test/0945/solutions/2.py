n = int(input())
a = list(map(int, input().split()))
b = a[:]
b.sort()
ok = 0
c = {}
g = {}
for i in range(n - 1):
    (l, r) = (b.index(a[i]), b.index(a[i + 1]))
    c[b[l]] = r
    g[r] = l
for i in range(n - 1):
    if not b[i] in c:
        continue
    if i > c[b[i]]:
        (l, r) = (c[b[i]], i)
    else:
        (l, r) = (i, c[b[i]])
    for j in range(l + 1, r):
        if b[j] in c:
            if c.get(b[j]) > r or c.get(b[j]) < l:
                ok = 1
                break
        if j in g:
            if g[j] > r or g[j] < l:
                ok = 1
                break
if ok:
    print('yes')
else:
    print('no')
