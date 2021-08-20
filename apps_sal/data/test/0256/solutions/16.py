x = [tuple((int(i) for i in input().split())) for j in range(4)]
if x[0][0] + x[1][1] > x[0][1] + x[1][0]:
    t1atk = x[1][1]
    t1def = x[0][0]
else:
    t1atk = x[0][1]
    t1def = x[1][0]


def f():
    if t1atk > t2def and t1def > t2atk:
        return 0
    elif t1atk < t2def and t1def < t2atk:
        return 2
    else:
        return 1


t2def = x[2][0]
t2atk = x[3][1]
a = f()
t2def = x[3][0]
t2atk = x[2][1]
b = f()
if a > b:
    t2def = x[2][0]
    t2atk = x[3][1]
else:
    t2def = x[3][0]
    t2atk = x[2][1]
if t1atk > t2def and t1def > t2atk:
    print('Team 1')
elif t1atk < t2def and t1def < t2atk:
    print('Team 2')
else:
    print('Draw')
