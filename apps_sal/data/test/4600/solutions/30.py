(N, M) = map(int, input().split(' '))
ac_set = set()
wa_cnt_list = [0] * N
(ac_cnt, wa_cnt) = (0, 0)
for i in range(M):
    (num, res) = input().split(' ')
    num = int(num) - 1
    if num not in ac_set:
        if res == 'AC':
            ac_cnt += 1
            wa_cnt += wa_cnt_list[num]
            ac_set.add(num)
        else:
            wa_cnt_list[num] += 1
print(ac_cnt, wa_cnt)
