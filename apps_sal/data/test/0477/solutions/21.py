(n, m, i, j, a, b) = map(int, input().split())
l = []
if (i - 1) % a == 0 and (j - 1) % b == 0:
    s1 = (i - 1) // a
    s2 = (j - 1) // b
    if (s1 + s2) % 2 == 0:
        l.append(max(s1, s2))
if (i - 1) % a == 0 and (m - j) % b == 0:
    s1 = (i - 1) // a
    s2 = (m - j) // b
    if (s1 + s2) % 2 == 0:
        l.append(max(s1, s2))
if (n - i) % a == 0 and (j - 1) % b == 0:
    s1 = (n - i) // a
    s2 = (j - 1) // b
    if (s1 + s2) % 2 == 0:
        l.append(max(s1, s2))
if (n - i) % a == 0 and (m - j) % b == 0:
    s1 = (n - i) // a
    s2 = (m - j) // b
    if (s1 + s2) % 2 == 0:
        l.append(max(s1, s2))
if (i, j) == (0, 0) or (i, j) == (n, m) or (i, j) == (n, 1) or ((i, j) == (1, m)):
    print(0)
elif i + a > n and i - a < 1:
    print('Poor Inna and pony!')
elif j + b > m and j - b < 1:
    print('Poor Inna and pony!')
elif len(l) == 0:
    print('Poor Inna and pony!')
else:
    print(min(l))
