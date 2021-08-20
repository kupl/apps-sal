tt = int(input())
for loop in range(tt):
    (x, y, z) = list(map(int, input().split()))
    if x == y == z:
        print('YES')
        print(x, y, z)
    elif x == y and x > z:
        print('YES')
        print(x, z, z)
    elif x == z and x > y:
        print('YES')
        print(y, x, y)
    elif y == z and y > x:
        print('YES')
        print(x, x, y)
    else:
        print('NO')
