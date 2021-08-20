n = int(input())
sum = 0
nums = {}
for _ in range(n):
    a = input()
    if a not in nums:
        nums[a] = 1
    else:
        nums[a] += 1
for i in list(nums.values()):
    sum += i % 2
print(sum)
