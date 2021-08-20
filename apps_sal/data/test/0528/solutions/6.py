(n, m) = [int(x) for x in input().split()]
d = {}
con = set()
for x in range(m):
    (a, b) = input().split()
    d.setdefault(a, {a}).add(b)
    d.setdefault(b, {b}).add(a)
res = None
for (x, y) in d.items():
    if x not in con:
        if all([d[u] == y for u in y]):
            con.update(y)
        else:
            res = 'NO'
            break
if not res:
    res = 'YES'
print(res)
