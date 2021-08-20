k = 'AHIMOTUVWXY'
l = 'iuvwo'
x = int(input())
y = list(map(int, input().split(' ')))
if (y.count(1) == x - 1 or y == [1]) and y != [0]:
    print('YES')
else:
    print('NO')
