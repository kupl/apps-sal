(n, k) = map(int, input().split())
h = sorted([int(input()) for _ in range(n)])
nums = [0] * (n - 1)
for i in range(n - 1):
    nums[i] = h[i + 1] - h[i]
ans = sum(nums[:k - 1])
t = sum(nums[:k - 1])
for i in range(k - 1, n - 1):
    t += nums[i] - nums[i - k + 1]
    if t < ans:
        ans = t
print(ans)
