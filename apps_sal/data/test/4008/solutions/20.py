n, k = map(int, input().split())
ar = list(map(int, input().split()))
s = set(ar)
d = dict()
for x in s:
    d[x] = 0
for x in ar:
    d[x] += 1
f = 1
for x in d:
    if d[x] > k:
        f = 0
if f == 0:
    print('NO')
else:
    z = ar[:]
    z = [[z[x], x, -1] for x in range(n)]
    z.sort(key=lambda x: x[0])
    w = 1
    for x in range(n):
        z[x][2] = w
        w = (w + 1) % k
        if w == 0:
            w = k
    z.sort(key=lambda x: x[1])
    print('YES')
    for x in z:
        print(x[2], end=' ')
