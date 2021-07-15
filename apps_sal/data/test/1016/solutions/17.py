n, m = map(int, input().split())
p = list(range(n + 1))
s = [{i} for i in p]
for i in range(m):
    x, y = map(int, input().split())
    x, y = p[x], p[y]
    if x != y:
        if len(s[x]) < len(s[y]):
            for k in s[x]:
                p[k] = y
                s[y].add(k)
            s[x].clear()
        else:
            for k in s[y]:
                p[k] = x
                s[x].add(k)
            s[y].clear()
q = 0
for p in s:
    if p: q += len(p) - 1
print(1 << q)
