a2 = input()
b2 = input()
a = []
b = []
for i in range(len(a2)):
    a.append(a2[i])
    b.append(b2[i])
k = 0
for i in range(len(a)):
    if i == 0 and len(a) > 1:
        if a[0] == '0' and b[0] == '0' and (a[1] == '0'):
            a[0] = 'X'
            b[0] = 'X'
            a[1] = 'X'
            k += 1
        elif a[0] == '0' and b[0] == '0' and (b[1] == '0'):
            a[0] = 'X'
            b[0] = 'X'
            b[1] = 'X'
            k += 1
    elif i == len(a) - 1 and len(a) > 1:
        if a[i] == '0' and b[i] == '0' and (a[i - 1] == '0'):
            a[i] = 'X'
            b[i] = 'X'
            a[i - 1] = 'X'
            k += 1
        elif a[i] == '0' and b[i] == '0' and (b[i - 1] == '0'):
            a[i] = 'X'
            b[i] = 'X'
            b[i - 1] = 'X'
            k += 1
    elif len(a) > 1:
        if a[i] == '0' and b[i] == '0' and (a[i - 1] == '0'):
            a[i] = 'X'
            b[i] = 'X'
            a[i - 1] = 'X'
            k += 1
        elif a[i] == '0' and b[i] == '0' and (b[i - 1] == '0'):
            a[i] = 'X'
            b[i] = 'X'
            b[i - 1] = 'X'
            k += 1
        elif a[i] == '0' and b[i] == '0' and (a[i + 1] == '0'):
            a[i] = 'X'
            b[i] = 'X'
            a[i + 1] = 'X'
            k += 1
        elif a[i] == '0' and b[i] == '0' and (b[i + 1] == '0'):
            a[i] = 'X'
            b[i] = 'X'
            b[i + 1] = 'X'
            k += 1
    else:
        k = 0
print(k)
