n, t = map(int, input().split())
l = list(map(int, input().split()))

nums = [0] * (n - 1)
for i in range(n - 1):
    nums[i] = l[i + 1] - l[i]

ans = t
m = 0
for i in nums:
    ans += min(i, t)
print(ans)
