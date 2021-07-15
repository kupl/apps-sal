a, b = [i for i in input().split()]
n = int(input())
pos = ['v', '<', '^', '>']
i = pos.index(a)
f1 = pos[(i + n) % 4]
f2 = pos[(i - n) % 4]
if f1 == f2:
    print('undefined')
elif f1 == b:
    print('cw')
elif f2 == b:
    print('ccw')
else:
    print('undefined')
