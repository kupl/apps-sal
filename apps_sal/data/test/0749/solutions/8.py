s = input()
letters = set(s)
ans = len(s)
for ch in letters:
	prev = -1
	max_dist = 0
	for pos in range(len(s)):
		if s[pos] == ch:
			max_dist = max(pos - prev - 1, max_dist)
			prev = pos
	max_dist = max(len(s) - prev - 1, max_dist)
	ans = min(ans, max_dist + 1)
print(ans)


