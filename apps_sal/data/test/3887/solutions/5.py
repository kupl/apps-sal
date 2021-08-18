a = list(input().split())
b, c = 1, 0
for i in a:
    if i == '-':
        c = c + 1
    elif i == '+':
        b = b + 1
    elif i != '?' and i != '=':
        n = int(i)
if b - c * n <= n and n <= b * n - c:
    print('Possible')
    b0 = []
    for i in range(b):
        b0.append(1)
    c0 = []
    for i in range(c):
        c0.append(1)

    x = b - c - n
    if x < 0:
        i = 0
        while x + n - 1 < 0:
            b0[i] = n
            x = x + n - 1
            i = i + 1
        if x != 0:
            b0[i] = -x + 1
    else:
        i = 0
        while x - n + 1 > 0:
            c0[i] = n
            x = x - n + 1
            i = i + 1
        if x != 0:
            c0[i] = x + 1
    s = str(b0[0])
    b = 1
    c = 0
    for i in a:
        if i == '-':
            s = s + ' - ' + str(c0[c])
            c = c + 1
        elif i == '+':
            s = s + ' + ' + str(b0[b])
            b = b + 1
        elif i == '=':
            print(s + ' = ' + str(n))
else:
    print('Impossible')
