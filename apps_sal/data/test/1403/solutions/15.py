(size, k) = input().split()
size = int(size)
k = int(k)
nums = input().split()
nums = [int(i) for i in nums]
occurances = {i: 0 for i in nums}
for num in nums:
    occurances[num] += 1
ans = []
nums = sorted(occurances.keys())
for i in range(len(nums) - 1):
    if not (nums[i] < nums[i + 1] and nums[i] + k >= nums[i + 1]):
        ans.append(nums[i])
ans.append(nums[-1])
ans_num = 0
for i in ans:
    ans_num += occurances[i]
print(ans_num)
