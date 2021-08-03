numbers = list([int(x) for x in input().split()])
nums = list([int(x) for x in input().split()])
t = numbers[1]

total = t
for i in range(1, len(nums)):
    check = nums[i] - nums[i - 1]
    total += check if check <= t else t

print(total)
