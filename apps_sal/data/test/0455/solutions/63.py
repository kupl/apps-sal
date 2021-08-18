def d_robot_arms(N, Pos):

    pos = []
    parity = (abs(Pos[0][0]) + abs(Pos[0][1])) % 2
    for x, y in Pos:
        parity_current = (abs(x) + abs(y)) % 2
        if parity != parity_current:
            return -1
        pos.append([x - y, x + y])

    arms = [1 << k for k in range(30, -1, -1)]
    if parity % 2 == 0:
        arms.append(1)

    ans_tmp = [str(len(arms)), ' '.join(list(map(str, arms)))]

    for pos_u, pos_v in pos:
        usum, vsum = 0, 0
        tmp = ''
        for arm_len in arms:
            if usum <= pos_u:
                udir = 'positive'
                usum += arm_len
            else:
                udir = 'negative'
                usum -= arm_len

            if vsum <= pos_v:
                vdir = 'positive'
                vsum += arm_len
            else:
                vdir = 'negative'
                vsum -= arm_len

            if udir == 'positive' and vdir == 'positive':
                tmp += 'R'
            elif udir == 'positive' and vdir == 'negative':
                tmp += 'D'
            elif udir == 'negative' and vdir == 'negative':
                tmp += 'L'
            else:
                tmp += 'U'
        ans_tmp.append(''.join(tmp))
    ans = '\n'.join(ans_tmp)
    return ans


N = int(input())
Pos = [[int(i) for i in input().split()] for j in range(N)]
print(d_robot_arms(N, Pos))
