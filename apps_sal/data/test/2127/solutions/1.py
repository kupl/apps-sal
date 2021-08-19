import sys
input = sys.stdin.readline
Q = int(input())
nx = 0
ny = 0
for i in range(Q):
    (q, x, y) = input().split()
    (x, y) = (int(x), int(y))
    if x > y:
        (x, y) = (y, x)
    if q == '+':
        nx = max(nx, x)
        ny = max(ny, y)
    elif x >= nx and y >= ny:
        print('YES')
    else:
        print('NO')
