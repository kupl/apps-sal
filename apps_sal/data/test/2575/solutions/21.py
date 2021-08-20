n = int(input())
for i in range(0, n):
    print('YES' if 360 % (180 - int(input())) == 0 else 'NO')
