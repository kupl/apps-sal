(pole1, pole2, pole3) = map(int, input().split())
if pole2 - pole1 == pole3 - pole2:
    print('YES')
else:
    print('NO')
