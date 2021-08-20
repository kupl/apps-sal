(x, y, z, t1, t2, t3) = list(map(int, input().split()))
lift = abs(z - x) * t2 + t3 + t3 + abs(x - y) * t2 + t3
stairs = t1 * abs(x - y)
if lift <= stairs:
    print('YES')
else:
    print('NO')
