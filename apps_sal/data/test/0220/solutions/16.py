(s, x) = map(int, input().split())
b = s - x
b = list(bin(s - x))
b = b[2:]
a = list(bin(x))
a = a[2:]
al = len(a)
bl = len(b)
c = []
if bl > al:
    for i in range(bl - al):
        c.append('0')
    c.extend(a)
    a = c
else:
    for i in range(al - bl):
        c.append('0')
    c.extend(b)
    b = c
p = 0
bl = len(b)
for i in range(bl - 1):
    if b[i] == '1':
        if a[i + 1] == '1':
            p = 1
bl = len(b)
if b[bl - 1] == '1':
    p = 1
if x > s:
    print('0')
elif p == 1:
    print('0')
elif s == x:
    print(2 ** a.count('1') - 2)
elif x == 0:
    print('1')
else:
    print(2 ** a.count('1'))
