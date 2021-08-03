n = int(input())
for i in range(n):
    x, y = [int(x) for x in input().split(' ')]
    if x == 1:
        if y == 1:
            print('YES')
        else:
            print('NO')
    elif x in [2, 3]:
        if y in [1, 2, 3]:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
