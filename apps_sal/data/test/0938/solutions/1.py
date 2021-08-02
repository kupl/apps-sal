a, b = map(int, input().split())
g = False
if b < a:
    g = True
    a, b = b, a
na = 0
nb = 0
n = 0
while a >= (na + 1) * na // 2:
    na += 1
na -= 1
if g == False:
    print(na)
sa = (na + 1) * na // 2
nb = na + 1
x = (na + 1) - (a - sa)
f = False
if a - sa != 0 and b >= x:
    f = True
    b -= x
    nb = na + 2
    if g == False:
        for i in range(na):
            if i != x - 1:
                print(i + 1, sep=' ', end=' ')
        print(na + 1, sep=' ', end=' ')
        print()
else:
    if g == False:
        for i in range(na):
            print(i + 1, sep=' ', end=' ')
        print()
h = nb
nb = 0
while b >= (2 * h + nb) * (nb + 1) // 2:
    nb += 1
nb -= 1
if f == False:
    print(nb + 1)
    for i in range(na, h + nb):
        print(i + 1, sep=' ', end=' ')
else:
    print(nb + 2)
    for i in range(na + 1, h + nb):
        print(i + 1, sep=' ', end=' ')
    print(x)
if g == True:
    print(na)
    if f == True:
        for i in range(na):
            if i != x - 1:
                print(i + 1, sep=' ', end=' ')
        print(na + 1, sep=' ', end=' ')
        print()
    else:
        for i in range(na):
            print(i + 1, sep=' ', end=' ')
        print()
