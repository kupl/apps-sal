input()
ax, ay = [int(i) for i in input().split()]
bx, by = [int(i) for i in input().split()]
cx, cy = [int(i) for i in input().split()]

bx -= ax
cx -= ax
by -= ay
cy -= ay

if bx * cx > 0 and by * cy > 0:
    print('YES')
else:
    print('NO')

