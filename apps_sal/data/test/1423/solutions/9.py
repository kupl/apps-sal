n, l, r = input().split(' ')
n = int(n)
l = int(l)
r = int(r)

at = input().split(' ')
pt = input().split(' ')

a = []
b = []
p = []
indices = []
for i in range(n):
    a.append(int(at[i]))
    p.append(int(pt[i]))
    b.append(None)
    indices.append(None)

for i in range(n):
    indices[p[i] - 1] = i

flag = True

i = 0
while (i < n):
    ind = indices[i]
    if i == 0:
        b[ind] = str(l)
        last = l - a[ind]
        i += 1
        continue

    exp = last + a[ind] + 1
    if exp > r:
        flag = False
        break

    exp = max([l, exp])

    last = exp - a[ind]
    b[ind] = str(exp)

    i += 1

if flag:
    print(' '.join(b))
else:
    print(-1)
