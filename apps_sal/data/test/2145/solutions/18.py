t = int(input())
for i in range(t):
    (x, y) = [int(i) for i in input().split(' ')]
    if x > 3:
        print('YES')
    elif x == 3 or x == 2:
        if y == 2 or y == 1 or y == 3:
            print('YES')
        else:
            print('NO')
    elif y == 1:
        print('YES')
    else:
        print('NO')
