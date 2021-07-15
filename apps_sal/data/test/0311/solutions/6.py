x, y, z, t1, t2, t3 = list(map(int, input().split()))
d1 = abs(x - y) * t1
d2 = abs(x - z) * t2 + abs(x - y) * t2 + 3 * t3
if d2 <= d1:
    print('YES')
else:
    print('NO')

