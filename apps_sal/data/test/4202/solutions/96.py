(L, R) = map(int, input().split())
MOD = 2019
if MOD <= R - L + 1:
    ans = 0
else:
    ans = MOD - 1
    nums = set()
    start = L % MOD
    for i in range(start, start + (R - L) + 1):
        if i % MOD in nums:
            break
        nums.add(i % MOD)
    nums = tuple(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            ans = min(ans, nums[i] * nums[j] % MOD)
print(ans)
