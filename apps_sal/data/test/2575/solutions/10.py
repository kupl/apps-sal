n = int(input())
for i in range(n):
    a = 180 - int(input())
    if 360 % a == 0:
        print('YES')
    else:
        print('NO')


