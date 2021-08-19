n = int(input())
nums = sorted(map(int, input().split()))
ans = 0
i = 0
ln = len(nums)
while i < ln // 2:
    ans += (nums[i] + nums[ln - i - 1]) ** 2
    i += 1
print(ans)
