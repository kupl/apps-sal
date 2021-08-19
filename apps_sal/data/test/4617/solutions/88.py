import math
b = input()
c = []
for i in range(len(b)):
    c.append(b[i])
f = input()
t = []
for i in range(len(f)):
    t.append(f[i])
d = []
for i in range(len(c)):
    d.append(c[-(i + 1)])
if d == t:
    print('YES')
else:
    print('NO')
