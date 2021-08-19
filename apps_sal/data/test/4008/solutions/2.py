(n, k) = list(map(int, input().split()))
d = {}
a = list(map(int, input().split()))
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
if max(d.values()) > k:
    print('NO')
else:
    print('YES')
    res = []
    x = 1
    s = {i: set() for i in set(a)}
    for i in range(k):
        res.append(x)
        s[a[i]].add(x)
        x += 1
    for i in range(k, n):
        z = 1
        while z in s[a[i]]:
            z += 1
        s[a[i]].add(z)
        res.append(z)
    print(*res)
