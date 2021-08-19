N = int(input())
nums = [int(s) for s in input().split()]
ans = max(nums) - min(nums)
print(ans)
