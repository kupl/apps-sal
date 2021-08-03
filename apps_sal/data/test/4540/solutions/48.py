n = int(input())
a = [0] + list(map(int, input().split())) + [0]

nums = [0] * (n + 1)
for i in range(n + 1):
    nums[i] = abs(a[i] - a[i + 1])

total = sum(nums)
for i in range(n):
    ans = total - nums[i] - nums[i + 1] + abs(a[i] - a[i + 2])
    print(ans)
