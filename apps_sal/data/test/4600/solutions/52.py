(N, M) = map(int, input().split(' '))
ac_set = set()
(wa_cnt_ls, wa_cnt) = ([0] * N, 0)
for i in range(M):
    (p, s) = input().split(' ')
    idx = int(p) - 1
    if not idx in ac_set:
        if s == 'AC':
            wa_cnt += wa_cnt_ls[idx]
            ac_set.add(idx)
        else:
            wa_cnt_ls[idx] += 1
print(len(ac_set), wa_cnt)
