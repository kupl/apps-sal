from math import floor
s = input()
sl = s.split(' ')
x = int(sl[0])
y = int(sl[1])
dis = abs(x) + abs(y)
if x > 0:
    if y > 0:
        print('0 {} {} 0'.format(dis, dis))
    else:
        print('0 {} {} 0'.format(-dis, dis))
elif y > 0:
    print('{} 0 0 {}'.format(-dis, dis))
else:
    print('{} 0 0 {}'.format(-dis, -dis))
