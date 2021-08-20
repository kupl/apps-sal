from sys import stdin, stdout
(d1, d2) = stdin.readline().rstrip().split()
n = int(stdin.readline().rstrip())
direction = []
for x in [d1, d2]:
    if x == '^':
        direction.append(0)
    elif x == '>':
        direction.append(1)
    elif x == '<':
        direction.append(3)
    else:
        direction.append(2)
n = n % 4
lTrue = False
rTrue = False
if (direction[0] + n) % 4 == direction[1]:
    lTrue = True
if (direction[0] - n) % 4 == direction[1]:
    rTrue = True
if lTrue and rTrue:
    print('undefined')
elif lTrue:
    print('cw')
else:
    print('ccw')
