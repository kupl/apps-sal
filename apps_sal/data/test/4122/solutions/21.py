import sys
from math import ceil

fin = sys.stdin.readline
H, n = [int(elem) for elem in fin().split()]
d_list = [int(elem) for elem in fin().split()]
prefix_sum_d = [0] * n
cur_sum = 0
for i, d in enumerate(d_list):
    cur_sum += d
    prefix_sum_d[i] = cur_sum

# no point of death during the first round and the hp does not increase
max_damage_in_round = -min(prefix_sum_d)
if H - max_damage_in_round > 0 and prefix_sum_d[-1] >= 0:
    print(-1)
    return

damage_per_round = -prefix_sum_d[-1]
if H <= max_damage_in_round:
    num_rounds_before_death = 0
else:
    num_rounds_before_death = ceil((H - max_damage_in_round) / damage_per_round)

rest_H = H - damage_per_round * num_rounds_before_death
past_minutes = num_rounds_before_death * n

for additional_minutes, gain in enumerate(prefix_sum_d, start=1):
    if rest_H + gain <= 0:
        print(additional_minutes + past_minutes)
        break

