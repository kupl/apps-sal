from collections import defaultdict
n = int(input())
factor_list = defaultdict(int)
for i in range(1, n + 1):
    p = 2
    t = i
    while p <= n ** 0.5 + 5:
        if t % p == 0:
            factor_list[p] += 1
            t //= p
        else:
            p += 1
    if t > 1:
        factor_list[t] += 1
nums = [0 for _ in range(1000)]
for (k, v) in list(factor_list.items()):
    nums[v] += 1
for i in range(998, -1, -1):
    nums[i] += nums[i + 1]
print(nums[74] + nums[24] * (nums[2] - 1) + nums[14] * (nums[4] - 1) + nums[4] * (nums[4] - 1) * (nums[2] - 2) // 2)
