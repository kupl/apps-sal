(x, y) = list(map(int, input().split(' ')))
(A_x, B_x, A_y, B_y) = (0, 0, 0, 0)
A = abs(x) + abs(y)
B = -A
if x < 0:
    A_x = B
    if y > 0:
        B_y = A
    else:
        B_y = B
else:
    B_x = A
    if y > 0:
        A_y = A
    else:
        A_y = B
print('%d %d %d %d' % (A_x, A_y, B_x, B_y))
