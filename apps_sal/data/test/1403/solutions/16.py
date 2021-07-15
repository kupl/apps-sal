n, k = list(map(int, input().split()))
last = 10000000
res = 0
cur_res = 1
for cur in sorted(list(map(int, input().split()))):
	if cur == last:
		cur_res += 1
	else:
		if cur > last+k:
			res += cur_res
		cur_res = 1
	last = cur
res += cur_res
print(res)

