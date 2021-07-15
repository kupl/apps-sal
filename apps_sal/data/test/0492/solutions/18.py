a = 'v<^>'
d = dict()
d['v'] = 0
d['<'] = 1
d['^'] = 2
d['>'] = 3
s, e = [d[x] for x in input().split()]
n = int(input()) % 4
flag_left = False
flag_right = False
if a[(s + n) % 4] == a[e]:
    flag_left = True
if a[(s - n) % 4] == a[e]:
    flag_right = True
if flag_left and flag_right:
    print('undefined')
elif flag_left:
    print('cw')
elif flag_right:
    print('ccw')
else:
    print('undefined')

