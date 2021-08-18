def robot_arms(N: int, XY: list) -> tuple:
    odd, even = 0, 0
    max_dist = 0
    for x, y in XY:
        ax, ay = abs(x), abs(y)
        if (ax + ay) % 2 == 0:
            even += 1
        else:
            odd += 1

        if max_dist < ax + ay:
            max_dist = ax + ay

    if odd == 0:
        arms = [1]
    elif even == 0:
        arms = []
    else:
        return [], []

    tmp, sum_tmp = 1, sum(arms)
    while sum_tmp < max_dist:
        arms.append(tmp)
        sum_tmp += tmp
        tmp <<= 1

    ops = []
    for x, y in XY:
        op = ''
        left_len = sum(arms)
        nx, ny = x, y
        for arm in reversed(arms):
            left_len -= arm
            if abs(nx + arm) + abs(ny) <= left_len:
                op = 'L' + op
                nx, ny = nx + arm, ny
            elif abs(nx - arm) + abs(ny) <= left_len:
                op = 'R' + op
                nx, ny = nx - arm, ny
            elif abs(nx) + abs(ny + arm) <= left_len:
                op = 'D' + op
                nx, ny = nx, ny + arm
            elif abs(nx) + abs(ny - arm) <= left_len:
                op = 'U' + op
                nx, ny = nx, ny - arm
        ops.append(op)

    return arms, ops


def __starting_point():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    ans = robot_arms(N, XY)

    if len(ans[0]) == 0:
        print((-1))
    else:
        d, w = ans
        print((len(d)))
        print((' '.join(map(str, d))))
        for ww in w:
            print(ww)


__starting_point()
