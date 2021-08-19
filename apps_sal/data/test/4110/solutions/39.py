# -*- coding: utf-8 -*-
D, G = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(D)]
ps, cs = list(zip(*data))
clear_cnt = D
min_prb = 1000
for i in range(1 << D):
    result = 0
    num_prb = 0
    not_selected_list = list()
    for j in range(D):
        if (i >> j & 1):
            result += ps[j] * 100 * (j + 1) + cs[j]
            num_prb += ps[j]
        else:
            not_selected_list.append(j)
    if result < G:
        not_selected = max(not_selected_list)
        add_num_prb = min(ps[not_selected], -(-(G - result) // (100 * (not_selected + 1))))
        num_prb += add_num_prb
        result += add_num_prb * (not_selected + 1) * 100
    if result >= G:
        min_prb = min(min_prb, num_prb)
print((int(min_prb)))
