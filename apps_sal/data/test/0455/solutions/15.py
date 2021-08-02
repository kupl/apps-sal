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
        # 偶数のみの場合は長さ 1 のアームが余計に必要
        arms = [1]
    elif even == 0:
        # 奇数のみの場合は 2 のべき乗の長さのアームだけで OK
        arms = []
    else:
        # 偶奇ごちゃ混ぜの場合は不成立
        return [], []

    # アームの準備
    tmp, sum_tmp = 1, sum(arms)
    while sum_tmp < max_dist:
        arms.append(tmp)
        sum_tmp += tmp
        tmp <<= 1

    # 各点へ腕を伸ばすための操作方法を決めていく
    ops = []
    for x, y in XY:
        op = ''
        # 決定操作
        # 長さが 2^m までの腕を使って届く範囲は綺麗な菱形になっている。
        # 点(x,y)から原点に向かって考える。
        # 腕の長い物から使っていき、使っていない腕で届く範囲に入っていく様に
        # 腕の方向を決定していく。
        # ただし、逆順に決定していくので、決定過程での方向と実際に出力すべき
        # 方向は逆になっていることに注意
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
