n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n - 1):
    if a[i] == 3:
        a[i] = '11'
    elif a[i] == 2:
        a[i] = '10'
    elif a[i] == 1:
        a[i] = '01'
    elif a[i] == 0:
        a[i] = '00'

for i in range(n - 1):
    if b[i] == 3:
        b[i] = '11'
    elif b[i] == 2:
        b[i] = '10'
    elif b[i] == 1:
        b[i] = '01'
    elif b[i] == 0:
        b[i] = '00'


def Checker(z, x, y):
    if z == '0':
        if x == '0' and y == '0':
            return '0'
        elif x == '0' and y == '1':
            return None
        elif x == '1' and y == '0':
            return '1'
        elif x == '1' and y == '1':
            return None
    elif z == '1':
        if x == '0' and y == '0':
            return None
        elif x == '0' and y == '1':
            return None
        elif x == '1' and y == '0':
            return '0'
        elif x == '1' and y == '1':
            return '1'


s = []
flag = True

for ti in ['00', '01', '10', '11']:
    t = ti
    if len(s) == n:
        break
    elif (Checker(t[0], a[0][0], b[0][0]) is not None) and (Checker(t[1], a[0][1], b[0][1]) is not None):
        s.append(t)
        for i in range(n - 1):
            c = Checker(t[0], a[i][0], b[i][0])
            e = Checker(t[1], a[i][1], b[i][1])
            if (c is not None) and (e is not None):
                k = ''.join([c, e])
                s.append(k)
                t = k
            else:
                s.clear()
                break
    elif t == '11':
        flag = False
if flag and s:
    print('YES')
    for i in range(n):
        if s[i] == '11':
            print(3, end=' ')
        elif s[i] == '10':
            print(2, end=' ')
        elif s[i] == '01':
            print(1, end=' ')
        elif s[i] == '00':
            print(0, end=' ')
else:
    print('NO')
