nums = list(map(int, input()))
num_len = len(nums)
sums = 0
for i in range(num_len):
    sums += nums[i]
if sums % 9 == 0:
    print('Yes')
else:
    print('No')
