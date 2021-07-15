d = {
	'U': (0, 1),
	'D': (0, -1),
	'L': (-1, 0),
	'R': (1, 0)
}


def compute_delta(s, head_idx, tail_idx):
	x = y = 0
	for i in range(head_idx, tail_idx):
		x, y = x + d[s[i]][0], y + d[s[i]][1]
	return [x, y]


n = int(input())
s = input()
dsc = list(map(int, input().split()))
total = compute_delta(s, 0, n)

l, r = 0, n
current_sol = -1
while l <= r:
	local_len = (r + l) // 2
	initial_diff = compute_delta(s, 0, local_len)
	local = [total[0] - initial_diff[0], total[1] - initial_diff[1]]
	is_possible = False
	diff = abs(dsc[0] - local[0]) + abs(dsc[1] - local[1])
	if diff <= local_len and (diff + local_len) % 2 == 0:
		is_possible = True
	for i in range(local_len, n):
		if is_possible:
			break
		d_old, d_new = d[s[i]], d[s[i - local_len]]
		local = [local[0] - d_old[0] + d_new[0], local[1] - d_old[1] + d_new[1]]
		diff = abs(dsc[0] - local[0]) + abs(dsc[1] - local[1])
		if diff <= local_len and (diff + local_len) % 2 == 0:
			is_possible = True
	if is_possible:
		current_sol = local_len
		r = local_len - 1
	else:
		l = local_len + 1
print(current_sol)

