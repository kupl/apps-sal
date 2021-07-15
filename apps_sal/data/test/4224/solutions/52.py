n = int(input())
nums = list(map(int,input().split()))
count = 0
even = False
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        even = True
    while even:
        if nums[i] % 2 == 0:
            count += 1
            nums[i] = int(nums[i]/2)
        else:
            even = False
print(count)
