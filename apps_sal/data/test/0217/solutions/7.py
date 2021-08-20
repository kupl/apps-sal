from sys import stdin, stdout
(a, b, f, k) = list(map(int, stdin.readline().rstrip().split()))
direction = 1
tank = b
refuels = 0
position = 0
if b < f or b < a - f:
    possible = False
else:
    possible = True
while k > 0 and possible == True:
    if k == 1 and tank >= a:
        k = 0
    elif k == 1:
        k = 0
        refuels += 1
    elif position == 0:
        position = f
        tank -= f
        direction = 1
    elif position == a:
        position = f
        tank -= a - f
        direction = -1
    elif direction == 1:
        if tank < 2 * (a - f):
            tank = b
            refuels += 1
            if b < 2 * (a - f):
                possible = False
        else:
            position = a
            direction = -1
            tank -= a - f
            k -= 1
    elif direction == -1:
        if tank < 2 * f:
            refuels += 1
            tank = b
            if b < 2 * f:
                possible = False
        else:
            position = 0
            direction = 1
            tank -= f
            k -= 1
if not possible:
    print(-1)
else:
    print(refuels)
