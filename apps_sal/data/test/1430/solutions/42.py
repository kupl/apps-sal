N, K=list(map(int,input().split()))
S = str(input())

# count sequence man and memo the cnt in group
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

# count max from evey
sum_list = []
end_pos = 2 * K if man_groups[0] > 0 else 2 * K - 1
end_pos = min(end_pos, len(man_groups) - 1)
last_max = sum(map(abs, man_groups[0: end_pos + 1]))
sum_list.append(last_max)
for i in range(1, len(man_groups)):
    if end_pos >= len(man_groups) - 1:
        break
    last_max -= abs(man_groups[i - 1])
    if man_groups[i] > 0:
        next_end_pos = min(end_pos + 2, len(man_groups) - 1)
        man_groups_to_add = man_groups[end_pos + 1: next_end_pos + 1]
        last_max += sum(map(abs, man_groups_to_add))
        end_pos = next_end_pos
    sum_list.append(last_max)

#print(sum_list)
#print(sum_list)
print((max(sum_list)))






