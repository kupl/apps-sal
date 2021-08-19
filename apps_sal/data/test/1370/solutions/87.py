def z(z_dic, v: int):
    if v in z_dic:
        return z_dic[v]
    z = 0
    if v == 2:
        z = 1
    elif v > 2:
        z = int(v * (v - 1) / 2)
    z_dic.setdefault(v, z)
    return z


def main():
    h, w, _k = list(map(int, input().split()))
    s = []
    for i in range(h):
        line = input()
        s_line = []
        for j in range(w):
            s_line.append(int(line[j]))
        s.append(s_line)

    ok_cnt_min = h * w
    op_cnt = h - 1  # すき間の個数
    for i in range(2 ** op_cnt):
        op = [False] * op_cnt
        for j in range(op_cnt):
            if ((i >> j) & 1):
                op[op_cnt - 1 - j] = True

        s2 = []
        current_sum = s[0]
        for k in range(op_cnt):
            if op[k]:
                s2.append(current_sum)
                current_sum = s[k + 1]
            else:
                next_sum = [(current_sum[a] + s[k + 1][a]) for a in range(w)]
                current_sum = next_sum

        s2.append(current_sum)
        s2len = len(s2)

        h_cut_cnt = len([x for x in op if x])
        if h_cut_cnt >= ok_cnt_min:
            break

        st = 0
        ed = 1
        cut_list = []
        dividable = True
        for j in range(1, w + 1):
            _sum_max = 0
            if ed <= j:
                ed = j
            else:
                continue

            _sum_max = max([sum(s2[_h][st:ed]) for _h in range(s2len)])
            if _sum_max > _k:
                if ed - st > 1:
                    cut_list.append(ed - 1)
                    st = ed - 1
                else:
                    dividable = False
                    break
        if not dividable:
            continue
        else:
            cnt = h_cut_cnt
            cnt += len(cut_list)
            if cnt < ok_cnt_min:
                ok_cnt_min = cnt

    print(ok_cnt_min)


main()
