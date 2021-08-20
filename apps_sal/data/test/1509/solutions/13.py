n = int(input())
nums = list(map(int, input().split()))
ans = nums[0] * (n - nums[0] + 1)
for i in range(1, n):
    if nums[i] > nums[i - 1]:
        ans += (nums[i] - nums[i - 1]) * (n - nums[i] + 1)
    elif nums[i] < nums[i - 1]:
        ans += (nums[i - 1] - nums[i]) * nums[i]
print(ans)
