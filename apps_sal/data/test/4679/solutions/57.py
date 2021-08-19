a = input()
b = input()
c = input()
a += 'A'
b += 'B'
c += 'C'
n = a
while True:
    if len(n) > 1:
        k = n[0]
        if n == a:
            a = a[1:]
        elif n == b:
            b = b[1:]
        else:
            c = c[1:]
        if k == 'a':
            n = a
        elif k == 'b':
            n = b
        else:
            n = c
    else:
        print(n[-1])
        break
