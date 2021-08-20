x = input()
pointindex = x.find('.')
if pointindex == -1:
    y = x.lstrip('0')
    print(y[0], end='')
    e = len(y) - 1
    z = y[1:].rstrip('0')
    if z != '':
        print('.' + z, end='')
    if e:
        print('E' + str(e))
elif x[:pointindex].lstrip('0') == '':
    z = x[pointindex + 1:].rstrip('0')
    for i in range(len(z)):
        if z[i] == '0':
            continue
        else:
            print(z[i], end='')
            e = -(i + 1)
            y = z[i + 1:].rstrip('0')
            if y != '':
                print('.' + y + 'E' + str(e))
            else:
                print('E' + str(e))
            break
else:
    y = x[:pointindex].lstrip('0')
    print(y[0], end='')
    e = len(y) - 1
    z = (y[1:] + x[pointindex + 1:]).rstrip('0')
    if z != '':
        print('.' + z, end='')
    if e:
        print('E' + str(e))
