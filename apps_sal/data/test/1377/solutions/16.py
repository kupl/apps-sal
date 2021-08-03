n = int(input().strip())
nums = list(map(int, input().strip().split()))
has_dups = (len(nums) > len(set(nums)))
mx = nums.index(max(nums))
if has_dups or nums[:mx + 1] != sorted(nums[:mx + 1]) or nums[mx:] != sorted(nums[mx:], reverse=True):
    print("NO")
else:
    print("YES")
