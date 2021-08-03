n, m = map(int, input().split())
a = set([int(input()) for _ in range(m)])

nums = [0] * (n + 1)
nums[0] = 1
if 1 not in a:
    nums[1] = 1
for i in range(2, n + 1):
    if i in a:
        continue
    nums[i] = nums[i - 1] + nums[i - 2]
print(nums[n] % 1000000007)
