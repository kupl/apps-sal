def d_robot_arms(N, Pos):
    # 参考: http://drken1215.hatenablog.com/entry/2018/09/30/002900

    pos = []
    # すべての座標でパリティが一致しなければ、条件を満たす腕を選べない
    parity = (abs(Pos[0][0]) + abs(Pos[0][1])) % 2
    for x, y in Pos:
        parity_current = (abs(x) + abs(y)) % 2
        if parity != parity_current:
            return -1
        pos.append((x - y, x + y))
        # u=x-y, v=x+y とすると、 点(u, v)は
        # 原点周りに45度回転させて距離√2倍にする座標変換で点(x, y)から移される点
        # あるいはu軸, v軸はx軸, y軸をそれぞれ原点周りに-45度回転させた軸

    # log2(10**9)=29.90 なので、2**30以下の2の冪乗を適当に選べば
    # xy平面上の x+y が奇数である任意の座標に到達できる
    arms = [1 << k for k in range(30, -1, -1)]
    if parity % 2 == 0:
        arms.append(1)  # x+yが偶数である座標に到達するときに必要

    # 腕の数, 長さのリストを最初に格納する(任意の入力に対して固定)
    ans_tmp = [str(len(arms)), ' '.join(list(map(str, arms)))]

    for u_pos, v_pos in pos:
        # u, v座標はそれぞれ独立に見て構わない
        u_sum, v_sum = 0, 0
        tmp = ''
        for arm_len in arms:
            u_dir = 1 if u_sum <= u_pos else -1
            u_sum += u_dir * arm_len

            v_dir = 1 if v_sum <= v_pos else -1
            v_sum += v_dir * arm_len

            # uv平面で軸と平行にどちら向きに移動するかと
            # xy平面での移動モード(UDLR)との対応
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
