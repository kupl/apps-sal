def input_sorted_int_list():
	return sorted(map(int, input().split()))

def update_moves_count_list(moves_count_list, tasks_list, from_left_to_right):
	p = 0
	for i in range(n + 1):
		if p < len(tasks_list) and i == tasks_list[p]:
			p += 1
		if from_left_to_right:
			moves_count_list[i] += len(tasks_list) - p
		else:
			moves_count_list[i] += p

k1, k2, k3 = list(map(int, input().split()))
n = k1 + k2 + k3

a = input_sorted_int_list()
b = input_sorted_int_list()
c = input_sorted_int_list()

left_moves_count = [0] * (n + 1)
right_moves_count = [0] * (n + 1)

update_moves_count_list(left_moves_count, a, True)
update_moves_count_list(left_moves_count, b, False)
update_moves_count_list(right_moves_count, b, True)
update_moves_count_list(right_moves_count, c, False)

r_cum_min = [None] * (n + 1)
r_cum_min[-1] = right_moves_count[n]

i = n - 1
while i >= 0:
	r_cum_min[i] = min(right_moves_count[i], r_cum_min[i + 1])
	i -= 1

answer = 1e9
for i in range(n + 1):
	if left_moves_count[i] + r_cum_min[i] < answer:
		answer = left_moves_count[i] + r_cum_min[i]

print(answer)

