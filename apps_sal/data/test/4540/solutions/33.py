n = int(input())
a = [0] + list(map(int, input().split())) + [0]

nums = [0] * (n + 1)
for i in range(1, n + 2):
    nums[i - 1] = abs(a[i] - a[i - 1])

ans = sum(nums)
for i in range(1, n + 1):
    print(ans - nums[i - 1] - nums[i] + abs(a[i + 1] - a[i - 1]))
