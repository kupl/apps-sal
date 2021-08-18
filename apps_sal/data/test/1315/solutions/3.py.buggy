N = int(input())
nums = list(map(int, input().split()))

for i in range(len(nums)):
    nums[i] += i

nums.sort()
for i in range(len(nums)):
    nums[i] -= i
    if i and nums[i] < nums[i - 1]:
        print(":(")
        return

print(' '.join(list(map(str, nums))))
