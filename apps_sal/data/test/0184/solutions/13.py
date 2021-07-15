l, r, a = list(map(int, input().split()))

best = 0

for l1 in range(l + 1):
	for r1 in range(r + 1):
		diff = abs(l1 - r1)

		if diff <= a:
			cur_ans = max(l1, r1) * 2 + (a - diff) // 2 * 2
			best = max(cur_ans, best)

print(best)

