(a, b) = map(int, input().split())
c = False
if b < a:
    c = True
    (a, b) = (b, a)
xa = 0
n = 0
while a >= (xa + 1) * xa // 2:
    xa += 1
xa -= 1
xb = 0
if c == False:
    print(xa)
sa = (xa + 1) * xa // 2
xb = xa + 1
x = xa + 1 - (a - sa)
flag = False
if a - sa != 0 and b >= x:
    flag = True
    b -= x
    xb = xa + 2
    if c == False:
        for i in range(xa):
            if i != x - 1:
                print(i + 1, sep=' ', end=' ')
        print(xa + 1, sep=' ', end=' ')
        print()
elif c == False:
    for i in range(xa):
        print(i + 1, sep=' ', end=' ')
    print()
r = xb
xb = 0
while b >= (2 * r + xb) * (xb + 1) // 2:
    xb += 1
xb -= 1
if flag == False:
    print(xb + 1)
    for i in range(xa, r + xb):
        print(i + 1, sep=' ', end=' ')
else:
    print(xb + 2)
    for i in range(xa + 1, r + xb):
        print(i + 1, sep=' ', end=' ')
    print(x)
if c == True:
    print(xa)
    if flag == True:
        for i in range(xa):
            if i != x - 1:
                print(i + 1, sep=' ', end=' ')
        print(xa + 1, sep=' ', end=' ')
        print()
    else:
        for i in range(xa):
            print(i + 1, sep=' ', end=' ')
        print()
