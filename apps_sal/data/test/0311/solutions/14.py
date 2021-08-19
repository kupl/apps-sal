(x, y, z, t1, t2, t3) = list(map(int, input().split()))
elevator = t2 * (abs(x - y) + abs(z - x)) + 3 * t3
stairs = t1 * abs(x - y)
if elevator > stairs:
    print('NO')
else:
    print('YES')
