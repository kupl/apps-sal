a ,b = list(map(int, input().split()))
if a == 0 and b == 0:
    print('NO')
else:
    if abs(a - b) < 2:
        print('YES')
    else:
        print('NO')

