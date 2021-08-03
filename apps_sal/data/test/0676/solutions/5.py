n = int(input())
a = sorted([int(input()) for _ in range(n)])
b = []

if n == 0:
    b = [1, 1, 3, 3]
elif n == 1:
    b = [a[0], a[0] * 3, a[0] * 3]
elif n == 2:
    x, y = a
    if x == y:
        b = [x * 3, x * 3]
    elif x * 3 >= y:
        b = [x * 3, 4 * x - y]
elif n == 3:
    x, y, z = a
    if x * 3 >= z and 4 * x == y + z:
        b = [3 * x]
    elif z % 3 == 0 and (z + z // 3) == x + y:
        b = [z // 3]
    elif z == 3 * x:
        b = [4 * x - y]
elif n == 4:
    if a[3] != a[0] * 3 or a[0] * 4 != a[1] + a[2]:
        b = [-1]

if len(b) + len(a) == 4:
    print('YES')
    for x in b:
        print(x)
else:
    print('NO')
