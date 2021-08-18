u = 0
v = 0


def f(c):
    nonlocal u
    nonlocal v
    if c == 'Q':
        u += 9
    elif c == 'R':
        u += 5
    elif c == 'B':
        u += 3
    elif c == 'N':
        u += 3
    elif c == 'P':
        u += 1
    elif c == 'q':
        v += 9
    elif c == 'r':
        v += 5
    elif c == 'b':
        v += 3
    elif c == 'n':
        v += 3
    elif c == 'p':
        v += 1


for i in range(8):
    for c in input():
        f(c)

if u == v:
    print('Draw')
elif u > v:
    print('White')
else:
    print('Black')
