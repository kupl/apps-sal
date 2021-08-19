s = input()
(a, temp) = s.split('.')
(d, b) = temp.split('e')
bb = int(b)
if a == '0':
    if d != '0':
        print(a, end='.')
        print(d)
    else:
        print(0)
elif bb == 0:
    if d != '0':
        print(a, end='.')
        print(d)
    else:
        print(a)
elif d == '0':
    print(a, end='')
    for i in range(bb):
        print('0', end='')
else:
    l = len(d)
    if l <= bb:
        print(a, end='')
        print(d, end='')
        temp2 = bb - l
        for i in range(temp2):
            print('0', end='')
    else:
        print(a, end='')
        for k in range(bb):
            print(d[k], end='')
        k += 1
        print('.', end='')
        print(d[k:])
