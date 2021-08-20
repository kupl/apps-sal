(n, m) = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
c = 0
res = []
for x in a:
    res.append((c + x) // m - c // m)
    c += x
print(' '.join([str(x) for x in res]))
