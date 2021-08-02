N, M = list(map(int, input().split()))
a = []
b = []
for i in range(M):
    x, y = list(map(int, input().split()))
    a.append(x)
    b.append(y)

c = []
d = []

for i in range(M):
    if a[i] == 1:
        c.append(b[i])

for i in range(M):
    if b[i] == N:
        d.append(a[i])

e = set(c) & set(d)

if len(e) != 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
