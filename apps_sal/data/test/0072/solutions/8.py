n = int(input())
m1 = 0
m2 = 0
m3 = 0
s1 = input()
s2 = input()
s3 = input()
x = len(s1)

for t in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
    m1 = max(m1, s1.count(t))
    m2 = max(m2, s2.count(t))
    m3 = max(m3, s3.count(t))
d = [[m1, 'Kuro'], [m2, 'Shiro'], [m3, 'Katie']]
d.sort()
if (d[2][0] == x) and (n == 1):
    if (d[1][0] == x):
        if (d[0][0] == x - 1):
            print(d[0][1])
        else:
            print('Draw')
    else:
        if (d[1][0] == x - 1):
            if d[0][0] == x - 1:
                print('Draw')
            else:
                print(d[1][1])
        else:
            if d[1][0] == x - 2:
                print('Draw')
            else:
                print(d[2][1])

elif d[1][0] + n >= x:
    print('Draw')
else:
    if m1 > max(m2, m3):
        print('Kuro')
    else:
        if m2 > max(m1, m3):
            print('Shiro')
        else:
            if m3 > max(m2, m1):
                print('Katie')
            else:
                print('Draw')
