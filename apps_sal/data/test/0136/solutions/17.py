a = str(input())
b = str(input())

a = a.lstrip('0')

b = b.lstrip('0')
flag = True

if len(a) > len(b):
    print(">")
    flag = False
elif len(a) < len(b):
    print('<')
    flag = False


if flag:
    flag1 = True

    for i in range(len(a)):
        if (int(a[i]) > int(b[i])):
            print('>')
            flag1 = False
            break
        if  (int(a[i]) < int(b[i])):
            print("<")
            flag1 = False
            break

    if (flag1):
        print('=')
