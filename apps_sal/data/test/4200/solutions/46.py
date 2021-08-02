n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort(reverse=True)
ss = sum(nums)
if nums[m - 1] * (4 * m) < ss:
    print('No')
else:
    print('Yes')
