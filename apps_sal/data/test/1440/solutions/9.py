n = int(input())
size___nr = [int(x) for x in input().split()]

one_idxes = [i for i, x in enumerate(size___nr) if x == 1]

curr_max = n - 1
ans = 0
while True:
	if curr_max == 0 or len(one_idxes) == 0:
		break
	if size___nr[curr_max] == 0:
		curr_max -= 1
		continue
	if size___nr[curr_max] == 3:
		size___nr[curr_max] = 0
		ans += 1
		curr_max -= 1
		continue
	elif size___nr[curr_max] == 1:
		size___nr[curr_max] -= 1
		one_idxes.pop()
		continue
	elif len(one_idxes) > 0:
		x = one_idxes.pop()
		size___nr[curr_max] -= 2
		size___nr[x] -= 1
		ans += 1
		if size___nr[curr_max] == 1:
			size___nr[curr_max] -= 1
		continue

ans += sum(size___nr) // 3
print(ans)

