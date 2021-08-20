n = int(input())
a = []
for i in range(n):
    k = input()
    (s, t) = (0, 0)
    for j in k:
        if j == 's':
            s += 1
        else:
            t += 1
    if t > 0:
        a.append([k, s / t])
    else:
        a.append([k, 100000])
a.sort(key=lambda x: x[1])
a = list(reversed(a))
l = a[0][0][0]
x = 0
m = []
for i in a:
    for j in i[0]:
        if j != l:
            m.append(x)
            x = 1
            l = j
        else:
            x += 1
m.append(x)
if a[0][0][0] == 'h':
    m = m[1:]
(p, q) = ([], [])
e = 0
z = len(m)
for i in range(z):
    if i % 2 == 0:
        p.append(m[i])
m = list(reversed(m))
if z % 2 == 1:
    m = m[1:]
    z -= 1
for i in range(z):
    if i % 2 == 0:
        e += m[i]
        q.append(e)
q = list(reversed(q))
ans = 0
for i in range(z // 2):
    ans += p[i] * q[i]
print(ans)
