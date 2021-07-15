n, m = list(map(int, input().split()))
l_list, r_list = [], []

for i in range(m):
	l, r = list(map(int, input().split()))
	l_list.append(l)
	r_list.append(r)

limit_min = max(l_list)
limit_max = min(r_list)
cnt = 0

for i in range(1, n + 1):
	if limit_min <= i <= limit_max:
		cnt += 1

print(cnt)

