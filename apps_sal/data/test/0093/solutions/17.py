from collections import deque
f = []
s = []
h = input()
h1 = input()
h = h + h1[::-1]
for i in h:
    if i != 'X':
        f.append(i)
h = input()
h1 = input()
h = h + h1[::-1]
for i in h:
    if i != 'X':
        s.append(i)
f1 = []
f1.append(f[1])
f1.append(f[2])
f1.append(f[0])
f2 = []
f2.append(f[2])
f2.append(f[0])
f2.append(f[1])
if f1 == s or f2 == s or f == s:
    print('YES')
else:
    print('NO')
