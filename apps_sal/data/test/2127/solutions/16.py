import sys
tc = int(sys.stdin.readline())
x = 0
y = 0
for i in range(tc):
    (p, a, b) = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    if p == '+':
        x = max(x, max(a, b))
        y = max(y, min(a, b))
    elif max(a, b) >= x and min(a, b) >= y:
        print('YES')
    else:
        print('NO')
