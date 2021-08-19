N = int(input().strip())
S_list = [input().strip() for _ in range(N)]


def count_brackets(brackets):
    cnt = 0
    min_cnt = 0
    for i in range(len(brackets)):
        if brackets[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            min_cnt = min(min_cnt, cnt)
    return (cnt, min_cnt)


tmp_cnt_plus = []
tmp_cnt_minus = []
for S in S_list:
    (cnt, min_cnt) = count_brackets(S)
    if cnt == min_cnt == 0:
        continue
    if cnt >= 0:
        tmp_cnt_plus.append((cnt, min_cnt))
    else:
        tmp_cnt_minus.append((cnt, min_cnt))
tmp_cnt_plus.sort(key=lambda x: -x[1])
tmp_cnt_minus.sort(key=lambda x: -(x[0] - x[1]))
sum_bracket = 0
flag = True
for (cnt, min_cnt) in tmp_cnt_plus + tmp_cnt_minus:
    if sum_bracket + min_cnt < 0:
        flag = False
        break
    sum_bracket += cnt
if sum_bracket == 0 and flag:
    print('Yes')
else:
    print('No')
