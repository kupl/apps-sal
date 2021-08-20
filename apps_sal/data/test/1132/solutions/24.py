(n, m) = map(int, input().split())
a = []
for h in range(0, n + 1):
    a.append([])
for i in range(m):
    (k, j) = map(int, input().split())
    a[k].append(j)
    a[j].append(k)
d2 = 0
d1 = 0
d3 = 0
for u in a:
    if len(u) == 1:
        d1 += 1
    if len(u) == 2:
        d2 += 1
    if len(u) == n - 1:
        d3 += 1
if d1 == 2 and d2 == n - 2:
    print('bus topology')
elif d3 == 1 and d1 == n - 1:
    print('star topology')
elif d2 == n:
    print('ring topology')
else:
    print('unknown topology')
