(x, y, z, t1, t2, t3) = map(int, input().split())
a = abs(x - y) * t1
b = abs(x - z) * t2 + abs(x - y) * t2 + t3 * 3
if a < b:
    print('NO')
else:
    print('YES')
