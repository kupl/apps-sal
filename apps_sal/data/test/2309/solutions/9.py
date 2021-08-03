n = int(input())
words = [input() for i in range(n)]

d = {}
for w in words:
    vs = "".join([c if c in 'aeiou' else '' for c in w])
    v = len(vs)
    last = vs[-1]
    if not v in d:
        d[v] = {}
    dd = d[v]
    if not last in dd:
        dd[last] = []
    dd[last].append(w)

pairs = []
e = {}
for v, dd in list(d.items()):
    for c, l in list(dd.items()):
        while len(l) > 1:
            p = l.pop(), l.pop()
            pairs.append(p)
        if len(l) > 0:
            if v in e:
                e[v] += l
            else:
                e[v] = l

ans = []
for c, l in list(e.items()):
    while len(l) > 1 and len(pairs) > 0:
        a = l.pop(), l.pop()
        for i, j in zip(a, pairs.pop()):
            ans.append((i, j))

while len(pairs) > 1:
    for i, j in zip(pairs.pop(), pairs.pop()):
        ans.append((i, j))

print(len(ans) // 2)
for i, j in ans:
    print(i, j)
