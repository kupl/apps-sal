from sys import stdin

data = stdin.readline().rstrip().split()
n = int(stdin.readline().rstrip()) % 4

dmap = {
    '^': 0,
    '>': 1,
    'v': 2,
    '<': 3
}
a, b = dmap[data[0]], dmap[data[1]]

if (a + n) % 4 == b and (a - n) % 4 == b:
    print('undefined')
elif (a + n) % 4 == b:
    print('cw')
else:
    print('ccw')

