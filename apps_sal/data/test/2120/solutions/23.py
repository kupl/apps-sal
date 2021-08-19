(n, m) = [int(x) for x in input().split()]
v = [int(x) for x in input().split()]
a = [[] for x in range(n)]
used = [0] * n
for i in range(m):
    (x, y) = [int(x) for x in input().split()]
    x -= 1
    y -= 1
    a[x].append(y)
    a[y].append(x)
l = sorted(zip(v, list(range(n))), key=lambda x: -x[0])
ans = 0
for (_, i) in l:
    used[i] = 1
    for x in a[i]:
        if not used[x]:
            ans += v[x]
print(ans)
