def foo(nums):
    res = 1
    flag = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            flag = 1
        if flag:
            res *= nums[i]
    return res


nums = list(map(int, list(input())))
res = foo(nums)
for i in range(len(nums)):
    nums2 = nums[:i]
    if nums[i] != 0:
        nums2.append(nums[i] - 1)
        for j in range(len(nums) - i - 1):
            nums2.append(9)
        res = max(res, foo(nums2))
print(res)
