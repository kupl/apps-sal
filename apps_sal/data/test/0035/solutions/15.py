n, m = map(int, input().split())
a = []
s = ''
for i in range(n):
    a.append(input())
    s += a[i]

s1 = ''
for i in range(m):
    for j in range(n):
        s1 += a[j][i]
f, f1 = True, True
v = []
v1 = []

if s[0:n * m // 3] == s[0] * (n * m // 3):
    v.append(s[0])
else:
    f = False
if s1[0:n * m // 3] == s1[0] * (n * m // 3):
    v1.append(s1[0])
else:
    f1 = False


if s[n * m // 3:n * m // 3 * 2] == s[n * m // 3] * (n * m // 3):
    v.append(s[n * m // 3])
else:
    f = False

if s1[n * m // 3:n * m // 3 * 2] == s1[n * m // 3] * (n * m // 3):
    v1.append(s1[n * m // 3])
else:
    f1 = False


if s[n * m // 3 * 2:n * m] == s[n * m // 3 * 2] * (n * m // 3):
    v.append(s[n * m // 3 * 2])
else:
    f = False
if s1[n * m // 3 * 2:n * m] == s1[n * m // 3 * 2] * (n * m // 3):
    v1.append(s1[n * m // 3 * 2])
else:
    f1 = False

v.sort()
v1.sort()
if f and v == ['B', 'G', 'R']:
    print('YES')
elif f1 and v1 == ['B', 'G', 'R']:
    print('YES')
else:
    print('NO')
