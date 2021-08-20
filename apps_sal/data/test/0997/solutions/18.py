s = input()
s1 = len(s)
i = 0
(a, b) = ([], [])
while i < s1:
    j = i
    k = ''
    while j < s1 and s[j] != ';' and (s[j] != ','):
        k += s[j]
        j += 1
    k1 = len(k)
    if k1 == 0:
        b.append(k)
    elif k1 > 1 and (k[0] == '-' or k[0] == '0'):
        b.append(k)
    else:
        fl = 1
        for m in range(k1):
            k2 = ord(k[m])
            if k2 >= 48 and k2 <= 57:
                continue
            else:
                fl = 0
                break
        if fl:
            a.append(k)
        else:
            b.append(k)
    i = j + 1
if s[-1] == ';' or s[-1] == ',':
    b.append('')
a1 = len(a)
b1 = len(b)
if a1 > 0:
    print('"', end='')
    for i in range(a1):
        print(a[i], end='')
        if i != a1 - 1:
            print(',', end='')
    print('"')
else:
    print('-')
if b1 > 0:
    print('"', end='')
    for i in range(b1):
        print(b[i], end='')
        if i != b1 - 1:
            print(',', end='')
    print('"')
else:
    print('-')
