n = int(input())
nums = [int(i) for i in input().split()]
extremums = 0
for i in range(1, n-1):
    if nums[i-1] < nums[i] > nums[i+1] or nums[i-1] > nums[i] < nums[i+1]:
        extremums += 1
print(extremums)

