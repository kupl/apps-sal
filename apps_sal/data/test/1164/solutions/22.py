def num(a):
    if len(a) < 4:
        return int(a) * 100
    q = 1
    if a[-3] != '.':
        q = 100
    b = ''
    for i in a:
        if i != '.':
            b += i
    print
    return int(b) * q

a = input()
b = 0
nn = ''
q = 2
for i in a:
    if i not in '1234567890.':
        if len(nn) > 0:
            b += num(nn)
        nn = ''
    else:
        nn += i
if len(nn) > 0:
    b += num(nn)
a = [b % 100]
b //= 100
while b != 0:
    a = [b % 1000] + a
    b //= 1000
if len(a) == 1:
    print(0, end='')
    if a[0] != 0:
        print('.', a[0] // 10, a[0] % 10, sep='')
else:
    if a[-1] == 0:
        for i in range(1, len(a)):
            a[i] = str(a[i]).zfill(3)
        a[0] = str(a[0])
        print('.'.join(a[:-1]))
    else:
        for i in range(1, len(a) - 1):
            a[i] = str(a[i]).zfill(3)
        a[-1] = str(a[-1]).zfill(2)
        a[0] = str(a[0])
        print('.'.join(a))
