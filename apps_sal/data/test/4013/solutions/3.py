n = int(input())
nums = sorted(list(map(int, input().split())))
r1 = nums[-2] - nums[0]
r2 = nums[-1] - nums[1]
print(min(r1, r2))
