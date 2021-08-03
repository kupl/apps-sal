class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        seen = {0: -1}
        prefix_sum = 0
        res = n = len(nums)
        for i, a in enumerate(nums):
            prefix_sum += a
            prefix_sum %= p
            seen[prefix_sum] = i
            if (target := (prefix_sum - need) % p) in seen:
                res = min(res, i - seen[target])
        return res if res < n else -1

        total = sum(nums)
        if (target := total % p) == 0:
            return 0
        # print(f\"total {total} target {target}\")
        left = 0
        prefix_sum = 0
        seen = {}
        ans = math.inf
        # looking for p*x + target
        for i, a in enumerate(nums):
            prefix_sum += a
            # print(f\"prefix_sum {prefix_sum}\")
            if ((prefix_sum - target) % p) in seen:
                ans = min(ans, i - seen[(prefix_sum - target) % p])
            seen[prefix_sum % p] = i
            # print(f\"added {prefix_sum%p}\")
        return -1 if ans >= len(nums) else ans
