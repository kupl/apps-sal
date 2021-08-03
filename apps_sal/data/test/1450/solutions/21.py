s = input()
l = len(s)
z = -1
c0 = 0
c1 = 0
c2 = 0
loc = -1
for i in range(l):
    c = s[i]
    if c == '0':
        c0 += 1
    if c == '1':
        c1 += 1
    if c == '2':
        c2 += 1
        if z == -1:
            z = c0
            loc = i
if z == -1:  # no 2
    for i in range(c0):
        print(0, end='')
    for i in range(c1):
        print(1, end='')
    print()
else:
    for i in range(z):
        print(0, end='')
    for i in range(c1):
        print(1, end='')
    for i in range(loc, l):
        if s[i] != '1':
            print(s[i], end='')
    print()
