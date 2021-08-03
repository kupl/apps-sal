s, f = input().strip().split()
n = int(input())
rot = ['^', '>', 'v', '<']
d = {'^': 0, '>': 1, 'v': 2, '<': 3}
cw = (d[s] + n) % 4
ccw = (d[s] - n) % 4
if cw == ccw:
    print('undefined')
elif rot[cw] == f:
    print('cw')
else:
    print('ccw')
