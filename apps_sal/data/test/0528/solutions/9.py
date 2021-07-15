n, m = [int(x) for x in input().split()]
d = {}
visited = set()
for x in range(m):
    a, b = input().split()
    d.setdefault(a, {a}).add(b)
    d.setdefault(b, {b}).add(a)
res='YES'
for x, y in d.items():
    if x not in visited:
        if all([d[u]==y for u in y]):
            visited.update(y)
        else:
            res='NO'
            break
print(res)
