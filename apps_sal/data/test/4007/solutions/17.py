n = int(input())
a = list(map(int, input().split()))
a = [-1] + a

z = []
s = []
f = []
r = [0] * (n + 1)
g = [0] * (n + 1)
for i in range(1, n+1):
    if a[i] != 0:
        g[i] = 1
        r[a[i]] = 1
for i in range(1, n + 1):
    if g[i] == 1 and r[i] == 0:
        s.append(i)
    elif g[i] == 0 and r[i] == 1:
        f.append(i)
    elif g[i] ==0 and r[i] == 0:
        z.append(i)
zp = 0
i = 1
# print(f)
# print(s)
for i in range(len(f)):
    # if i < len(f):
    fin = f[i]
    st = s[i]
    if (i == len(f) - 1) and len(z) == 1:
        a[z[0]] = st
        a[fin] = z[0]
        z.pop()
    else:
        a[fin] = st

if len(z) > 0:
    st = z[0]
    for i in range(len(z)):
        ze = z[i]
        if i < len(z) - 1:
            a[ze] = z[i + 1]
        else:
            a[ze] = st
print(*a[1:])



