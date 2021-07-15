from itertools import combinations

nums = [int(x) for x in input().split()]
average = sum(nums) / 2
for a, b, c in combinations(nums, 3):
	if a + b + c == average:
		print('YES')
		break
else:
	print('NO')

