a = [list(map(int, input().split())) for _ in range(3)]
b = list(zip(*a))
c = a[0]
d = b[0]
f = True

dx1 = c[1] - c[0]
dx2 = c[2] - c[1]
dy1 = d[1] - d[0]
dy2 = d[2] - d[1]

for i in range(3):
    c = a[i]
    d = b[i]
    if dx1 == c[1] - c[0] and dx2 == c[2] - c[1] and dy1 == d[1] - d[0] and dy2 == d[2] - d[1]:
        f = True
    else:
        f = False
        break
if f:
    print('Yes')
else:
    print('No')
