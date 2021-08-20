def __starting_point():
    (x, y, z, t1, t2, t3) = [int(i) for i in input().split(' ')]
    lift_time = (abs(z - x) + abs(y - x)) * t2 + 3 * t3
    stairs_time = abs(y - x) * t1
    if lift_time <= stairs_time:
        print('YES')
    else:
        print('NO')


__starting_point()
