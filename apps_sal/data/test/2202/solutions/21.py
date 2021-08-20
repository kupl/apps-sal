line1 = list(map(int, input().split()))
nums = list(map(int, input().split()))
(n, p) = (line1[0], line1[1])
sum_all = sum(nums)
sum_left = nums[0]
sum_right = sum_all - sum_left
res = sum_left % p + sum_right % p
for i in range(1, n - 1):
    sum_left += nums[i]
    sum_right -= nums[i]
    temp = sum_left % p + sum_right % p
    res = max(res, temp)
print(res)
