n = int(input())
nums = [int(x) for x in input().split()]
nums += nums
a = 0
res = 0
for i in nums:
	if i ==1:
		a += 1
		res = max(res, a)
	else:
		a = 0
print(res)
