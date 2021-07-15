n, m, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
paint = [list(map(int, input().split())) for i in range(n)]

if ((0 not in arr) and (len(set(arr)) > k)) or (len(set(arr)) - 1 > k):
	print(-1)
	return

#DP(index, color of index, current beauty)
dp = [0 for n_idx in range(n)]
for n_idx in range(n):
	dp[n_idx] = [0 for m_idx in range(m)]
	for m_idx in range(m):
		dp[n_idx][m_idx] = [float('inf') for k_idx in range(k + 1)]

#Initialize first list of DP
c0 = arr[0]
if c0 != 0: #first tree is already colored
	dp[0][c0 - 1][1] = 0
else:
	for color in range(m):
		dp[0][color][1] = paint[0][color]


for idx in range(1, n):
	min_last_idx = {}
	for beauty in range(max(1, k - (n - idx) + 1), min(k + 1, idx + 2)):
		#get min + 2nd min of all beauty - 1
		min_cost = float('inf')
		min_cost_color = -1
		sec_min_cost = float('inf')
		sec_min_cost_color = -1

		for color in range(m):
			next_cost = dp[idx - 1][color][beauty - 1]
			if next_cost < min_cost:
				sec_min_cost = min_cost
				sec_min_cost_color = min_cost_color
				min_cost = next_cost
				min_cost_color = color
			elif next_cost < sec_min_cost:
				sec_min_cost = next_cost
				sec_min_cost_color = color
		min_last_idx[beauty] = [[min_cost, min_cost_color], [sec_min_cost, sec_min_cost_color]]


	curr_color = arr[idx]
	if curr_color != 0: #current tree already colored
		for beauty in range(max(1, k - (n - idx) + 1), min(k + 1, idx + 2)):
			cost_prev_same_color = dp[idx - 1][curr_color - 1][beauty]
			min_cost, min_cost_color = min_last_idx[beauty][0]
			if min_cost_color == curr_color - 1:
				min_cost = min_last_idx[beauty][1][0]
			dp[idx][curr_color - 1][beauty] = min(cost_prev_same_color, min_cost)

	else:
		for curr_color in range(m):
			cost_to_color = paint[idx][curr_color]
			for beauty in range(max(1, k - (n - idx) + 1), min(k + 1, idx + 2)):
				cost_prev_same_color = dp[idx - 1][curr_color][beauty]
				min_cost, min_cost_color = min_last_idx[beauty][0]
				if min_cost_color == curr_color:
					min_cost = min_last_idx[beauty][1][0]
				dp[idx][curr_color][beauty] = cost_to_color + min(cost_prev_same_color, min_cost)

min_paint = min([l[k] for l in dp[n - 1]])
if min_paint != float('inf'):
	print(min_paint)
else:
	print(-1)



