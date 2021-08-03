n = int(input())
nums = [int(x) for x in input().split(' ')]
firstZero = nums.index(0)
lastZero = len(nums) - 1 - nums[::-1].index(0)

for i in range(len(nums[firstZero:])):
    if nums[firstZero + i] == 0:
        c = 0
    else:
        c += 1
    nums[firstZero + i] = c
nums = nums[::-1]
for i in range(len(nums)):
    if nums[i] == 0:
        c = 0
    else:
        c += 1

    if i > len(nums) - firstZero:
        nums[i] = c
        continue

    if nums[i] >= c or nums[i] < 0:
        nums[i] = c

print(' '.join([str(x) for x in nums[::-1]]))
