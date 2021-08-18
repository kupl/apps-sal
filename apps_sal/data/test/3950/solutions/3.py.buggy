def getRawInteger():
    return [int(x) for x in input().split()]


n, q = getRawInteger()
a = getRawInteger()

if n != len(a):
    raise ValueError('n is not correct.')

l, r = [n] * (q + 5), [0] * (q + 5)
f = [i for i in range(n + 5)]


def getRoot(u):
    while f[u] != u:
        f[u] = f[f[u]]
        u = f[f[u]]
    return u


for i in range(n):
    l[a[i]] = min(l[a[i]], i)
    r[a[i]] = max(r[a[i]], i)
if l[q] > r[q]:
    if l[0] > r[0]:
        print('NO')
        return
    a[l[0]] = q
    f[l[0]] = getRoot(l[0] + 1)
for i in reversed(list(range(1, q + 1))):
    it = getRoot(l[i])
    while it <= r[i]:
        if a[it] < i and a[it]:
            print('NO')
            return
        a[it] = i
        f[it] = getRoot(it + 1)
        it = getRoot(it)
out = 'YES\n'
for x in a:
    if x:
        out += str(x) + ' '
    else:
        out += '1 '
print(out)
