n, w = list(map(int, input().split()))
cur_delta = max_delta = min_delta = 0
for ai in map(int, input().split()):
	cur_delta += ai
	max_delta = max(max_delta, cur_delta)
	min_delta = min(min_delta, cur_delta)
min_res = 0-min_delta
max_res = w-max_delta
if max_res < min_res:
	print('0')
else:
	print(max_res+1-min_res)

