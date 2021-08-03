nums = list(map(int, input().split()))
nums.sort(reverse=True)

ans = nums[0] - nums[1]
nums[1] = nums[0]
nums[2] += ans
ans += (nums[0] - nums[2]) // 2

if (nums[0] - nums[2]) % 2 == 1:
    print(ans + 2)
elif (nums[0] - nums[2]) % 2 == 2:
    print(ans + 1)
else:
    print(ans)
