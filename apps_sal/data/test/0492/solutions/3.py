(s, e) = input().split()
d = dict()
d['^'] = 0
d['<'] = 1
d['v'] = 2
d['>'] = 3
n = int(input()) % 4
s = d[s]
e = d[e]
l = 0
r = 0
if (n + s) % 4 == e:
    l = 1
if (s - n) % 4 == e:
    r = 1
if l + r == 2:
    print('undefined')
elif r == 1:
    print('cw')
else:
    print('ccw')
