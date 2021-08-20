def index(lena):
    if lena == 8:
        return 4
    elif lena == 7:
        return 9
    elif lena == 6:
        return 14
    elif lena == 5:
        return 19
    elif lena == 4:
        return 24
    elif lena == 3:
        return 29
    elif lena == 2:
        return 34
    elif lena == 1:
        return 39


s = int(input())
ip = []
for a in range(s):
    q = input().split(':')
    q1 = []
    c = 0
    for a in q:
        if a == '' and c == 0:
            q1.append(a)
            c = 1
        elif a == '' and c == 1:
            pass
        else:
            q1.append(a)
    ip.append(q1)
for a in ip:
    s = []
    lena = len(a)
    z = '0000:0000:0000:0000:0000:0000:0000:0000'
    for i in range(lena):
        if a[i] == '':
            s.append(z[:index(lena)])
        else:
            q = '{0:0>4}'.format(a[i])
            s.append(q)
    res = ':'.join(s)
    print(res)
