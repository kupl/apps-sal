def get_len_sq(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


(ax, ay, bx, by, cx, cy) = list(map(int, input().split()))
a = (ax, ay)
b = (bx, by)
c = (cx, cy)
f = get_len_sq
if f(a, b) == f(b, c):
    if a[0] + c[0] == 2 * b[0] and a[1] + c[1] == 2 * b[1]:
        print('No')
    else:
        print('Yes')
else:
    print('No')
