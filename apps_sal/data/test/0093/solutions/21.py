a = input()
b = input()[::-1]
s1 = ''
if a[0] != 'X':
    s1 += a[0]
if a[1] != 'X':
    s1 += a[1]
if b[0] != 'X':
    s1 += b[0]
if b[1] != 'X':
    s1 += b[1]
a = input()
b = input()[::-1]
s2 = ''
if a[0] != 'X':
    s2 += a[0]
if a[1] != 'X':
    s2 += a[1]
if b[0] != 'X':
    s2 += b[0]
if b[1] != 'X':
    s2 += b[1]
c = s2.index(s1[0])
if s2[(c + 1) % 3] == s1[1]:
    print("YES")
else:
    print('NO')
