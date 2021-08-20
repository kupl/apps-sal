n = int(input().strip())
nums = list(map(int, input().strip().split()))
res = []
for i in range(n - 1):
    if nums[i] >= nums[i + 1]:
        res.append(nums[i])
res.append(nums[n - 1])
print(len(res))
print(' '.join(list(map(str, res))))
