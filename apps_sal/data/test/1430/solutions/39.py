N, K = list(map(int, input().split()))
S = str(input())

man_groups = []
same_cnt = 0
last_man = ""
for i in range(N):
    cur_man = S[i]
    if cur_man != last_man:
        if same_cnt > 0:
            if last_man == "0":
                same_cnt *= -1
            man_groups.append(same_cnt)
        same_cnt = 1
    else:
        same_cnt += 1
    last_man = cur_man
if same_cnt > 0:
    if last_man == "0":
        same_cnt *= -1
    man_groups.append(same_cnt)

sum_list = []
end_pos = 2 * K if man_groups[0] > 0 else 2 * K - 1
max_man_groups_idx = len(man_groups) - 1
end_pos = min(end_pos, max_man_groups_idx)
last_max = sum(map(abs, man_groups[0: end_pos + 1]))
sum_list.append(last_max)

start_pos = 2 if man_groups[0] > 0 else 1
for i in range(start_pos, len(man_groups), 2):
    if end_pos >= max_man_groups_idx:
        break
    for j in range(2):
        idx = i - j - 1
        if idx >= 0:
            last_max -= abs(man_groups[idx])
    for j in range(2):
        end_pos += 1
        if end_pos <= max_man_groups_idx:
            last_max += abs(man_groups[end_pos])
    sum_list.append(last_max)

print((max(sum_list)))
