a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a % 10 == 0:
    aa = 99
    aaa = a
else:
    aa = a % 10
    aaa = ((a // 10) + 1) * 10

if b % 10 == 0:
    bb = 99
    bbb = b
else:
    bb = b % 10
    bbb = ((b // 10) + 1) * 10

if c % 10 == 0:
    cc = 99
    ccc = c
else:
    cc = c % 10
    ccc = ((c // 10) + 1) * 10

if d % 10 == 0:
    dd = 99
    ddd = d
else:
    dd = d % 10
    ddd = ((d // 10) + 1) * 10

if e % 10 == 0:
    ee = 99
    eee = e
else:
    ee = e % 10
    eee = ((e // 10) + 1) * 10

if min(aa, bb, cc, dd, ee) == 99:
    print(a + b + c + d + e)
    return

print(aaa + bbb + ccc + ddd + eee - (10 - min(aa, bb, cc, dd, ee)))
