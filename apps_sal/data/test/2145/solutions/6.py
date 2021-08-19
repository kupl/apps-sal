a = int(input())
for i in range(a):
    (x, y) = map(int, input().split())
    if x >= 4:
        print('YES')
    elif y <= x:
        print('YES')
    elif x == 2 and y == 3:
        print('YES')
    else:
        print('NO')
