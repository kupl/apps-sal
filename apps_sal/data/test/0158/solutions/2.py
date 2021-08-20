n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
if nums[len(nums) // 2 - 1] < nums[len(nums) // 2]:
    print('YES')
else:
    print('NO')
