k, m = input().split()
n = int(input())

n %= 4
a = ['v', '<', '^', '>', 'v', '<', '^', '>']
if n == 2 or n == 0:
    print('undefined')
if n == 1:
    if m == a[a.index(k) + 1]:
        print('cw')
    else:
        print('ccw')
if n == 3:
    if m == a[a.index(k) + 3]:
        print('cw')
    else:
        print('ccw')
