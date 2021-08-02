n = int(input())
a = [0] + list(map(int, input().split())) + [0]

nums = [0] * (n + 1)
for i in range(n + 1):
    nums[i] = abs(a[i] - a[i + 1])

t = sum(nums)
for i in range(1, n + 1):
    ans = t - (nums[i - 1] + nums[i]) + abs(a[i - 1] - a[i + 1])
    print(ans)
