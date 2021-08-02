a = input()
b = input()
c = input()

d = 'A'
while True:
    if d == 'A':
        if len(a) == 0:
            break
        s = a[0]
        a = a[1:]
    elif d == 'B':
        if len(b) == 0:
            break
        s = b[0]
        b = b[1:]
    else:
        if len(c) == 0:
            break
        s = c[0]
        c = c[1:]
    if s == 'a':
        d = 'A'
    elif s == 'b':
        d = 'B'
    else:
        d = 'C'
print(d)
