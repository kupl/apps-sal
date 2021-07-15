t = input().split(',')
w = t[::2]
c = list(map(lambda x : int(x), t[1::2]))

max_d = 0
cur_d = 0
cnt = [10**6]

ans = [[] for i in range(10**6)]


i = 0
while i < len(w):
	ans[cur_d].append(w[i])
	cnt[cur_d] -= 1
	if c[i] > 0:
		cnt.append(c[i])
		cur_d += 1
		max_d = max(max_d, cur_d)
	else:
		while cnt[cur_d] == 0:
			cnt.pop()
			cur_d -= 1
	i += 1


print(max_d + 1)
for i in range(max_d + 1):
	print(' '.join(ans[i]))
