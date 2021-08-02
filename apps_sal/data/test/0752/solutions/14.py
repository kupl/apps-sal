def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = int(input())
a = [input().strip() for i in range(n)]
b = [input().strip() for i in range(n)]

ans = 0
c = [0, 0, 0]
d = [0, 0, 0]
for i, ss in enumerate(['S', 'L', 'M']):
    c[i] = a.count(ss)
    d[i] = b.count(ss)
    x = min(c[i], d[i])
    c[i] -= x
    d[i] -= x
ans += sum(d)
c = [0, 0]
d = [0, 0]
for i, ss in enumerate(['XS', 'XL']):
    c[i] = a.count(ss)
    d[i] = b.count(ss)
    x = min(c[i], d[i])
    c[i] -= x
    d[i] -= x
ans += sum(d)
c = [0, 0]
d = [0, 0]
for i, ss in enumerate(['XXS', 'XXL']):
    c[i] = a.count(ss)
    d[i] = b.count(ss)
    x = min(c[i], d[i])
    c[i] -= x
    d[i] -= x
ans += sum(d)
c = [0, 0]
d = [0, 0]
for i, ss in enumerate(['XXXS', 'XXXL']):
    c[i] = a.count(ss)
    d[i] = b.count(ss)
    x = min(c[i], d[i])
    c[i] -= x
    d[i] -= x
ans += sum(d)

print(ans)
