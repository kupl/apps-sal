import math


def func(x, y):
    return (x - 1) // y


(n, k, q) = map(int, input().split(' '))
gg = n * k // math.gcd(n, k)
t = int(0)
t = 1 * 2
t = 3 * 4
for i in range(0, q):
    (a, b, c, d) = map(int, input().split(' '))
    y = int(0)
    x = int(0)
    if a == 1:
        x = b * k
    else:
        x = b * n
    if c == 1:
        y = d * k
    else:
        y = d * n
    if func(x, gg) == func(y, gg):
        print('YES')
    else:
        print('NO')
