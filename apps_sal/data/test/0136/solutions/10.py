a = input()
b = input()


def delL(inp):
    out = ''
    flag = False
    for i in inp:
        if i != '0':
            flag = True
        if flag:
            out = out + i
    if out == '':
        return '0'
    return out


a = delL(a)
b = delL(b)

if len(a) > len(b):
    print('>')
elif len(a) < len(b):
    print('<')
else:
    flag = False
    for i in range(len(a)):
        if a[i] > b[i]:
            flag = True
            print('>')
            break
        elif a[i] < b[i]:
            flag = True
            print('<')
            break
    if flag == False:
        print('=')
