N, M = map(int, input().split(' '))
ac_set = set()
wa_cnt, wa_cnt_ls = 0, [0] * N
for i in range(M):
    p, s = input().split(' ')
    idx = int(p) - 1
    if not idx in ac_set:
        if s == 'AC':
            ac_set.add(idx)
            wa_cnt += wa_cnt_ls[idx]
        else:
            wa_cnt_ls[idx] += 1
print(len(ac_set), wa_cnt)
