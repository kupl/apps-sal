input()
res = 0
cur = 1
cur_p = 0
s = input()
for c in s:
	if c == "G":
		cur += 1
		cur_p += 1
		res = max(res, cur)
	else:
		cur = cur_p + 1
		cur_p = 0
print(min(res, s.count("G")))

