n = int(input())
a = list(map(int, input().split()))
ans = n
s = set()
x = {i: 0 for i in range(1, 100001)}
y = {}
for i in range(n):
    e = a[i]
    c = x[e]
    if c:
        y[c].remove(e)
        if len(y[c]) == 0:
            s.remove(c)
    x[e] += 1
    c += 1
    if c not in y:
        y[c] = set({e})
    else:
        y[c].add(e)
    s.add(c)
    if len(s) == 2:
        l = list(s)
        p = l[0]
        q = l[1]
        py = len(y[p])
        qy = len(y[q])
        if py == 1:
            if p == q + 1 or p == 1:
                ans = i + 1
        if qy == 1:
            if q == p + 1 or q == 1:
                ans = i + 1
print(ans)
