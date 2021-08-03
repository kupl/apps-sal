import sys
S = input()
x, y = list(map(int, input().split()))

f_first = S[0] == 'F'
x_moves = []
y_moves = []
x_dir = False
sp = S.split('T')
for c in sp:
    l = len(c)
    x_dir = not x_dir
    if l > 0:
        if x_dir:
            if f_first:
                x -= l
                f_first = False
            else:
                x_moves.append(l)
        else:
            y_moves.append(l)

x, y = abs(x), abs(y)
sum_x, sum_y = sum(x_moves), sum(y_moves)
if x > sum_x or y > sum_y:
    print('No')
    return


def ok(moves, summ, to):
    if len(moves) == 0:
        return to == 0
    ss = set([0])
    rem = summ
    for m1 in moves:
        rem -= m1
        _ss = set()
        for m2 in ss:
            if m2 + m1 <= to + rem:
                _ss.add(m2 + m1)
            if m2 - m1 >= to - rem:
                _ss.add(m2 - m1)
        ss = _ss
    return to in ss


print(('Yes' if ok(x_moves, sum_x, x) and ok(y_moves, sum_y, y) else 'No'))
