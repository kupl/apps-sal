def d_robot_arms(N, Pos):

    pos = []
    parity = (abs(Pos[0][0]) + abs(Pos[0][1])) % 2
    for x, y in Pos:
        parity_current = (abs(x) + abs(y)) % 2
        if parity != parity_current:
            return -1
        pos.append((x - y, x + y))

    arms = [1 << k for k in range(30, -1, -1)]
    if parity % 2 == 0:
        arms.append(1)

    ans_tmp = [str(len(arms)), ' '.join(list(map(str, arms)))]

    for u_pos, v_pos in pos:
        u_sum, v_sum = 0, 0
        tmp = ''
        for arm_len in arms:
            u_dir = 1 if u_sum <= u_pos else -1
            u_sum += u_dir * arm_len

            v_dir = 1 if v_sum <= v_pos else -1
            v_sum += v_dir * arm_len

            if u_dir == 1 and v_dir == 1:
                tmp += 'R'
            elif u_dir == 1 and v_dir == -1:
                tmp += 'D'
            elif u_dir == -1 and v_dir == -1:
                tmp += 'L'
            else:
                tmp += 'U'
        ans_tmp.append(''.join(tmp))
    ans = '\n'.join(ans_tmp)
    return ans


N = int(input())
Pos = [[int(i) for i in input().split()] for j in range(N)]
print(d_robot_arms(N, Pos))
