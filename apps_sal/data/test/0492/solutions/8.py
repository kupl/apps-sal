s, f = input().split(' ')
n = int(input())

cw = {'^': 1, '>': 2, 'v': 3, '<': 0}
ccw = {'^': 1, '>': 0, 'v': 3, '<': 2}

a = (cw[s] + n) % 4
b = (ccw[s] + n) % 4

if a == cw[f] and b == ccw[f]:
    print('undefined')
elif a == cw[f]:
    print('cw')
elif b == ccw[f]:
    print('ccw')
else:
    print('undefined')
