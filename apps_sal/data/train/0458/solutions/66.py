class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        seen = {0: -1}
        cur = 0
        res = n = len(nums)
        for i, a in enumerate(nums):
            cur = (cur + a) % p
            seen[cur] = i
            if (target := (cur - need) % p) in seen:
                res = min(res, i - seen[target])
        return res if res < n else -1

        total = sum(nums)
        if (target := total % p) == 0:
            return 0
        left = 0
        prefix_sum = 0
        seen = {}
        ans = math.inf
        for i, a in enumerate(nums):
            prefix_sum += a
            if ((prefix_sum - target) % p) in seen:
                ans = min(ans, i - seen[(prefix_sum - target) % p])
            seen[prefix_sum % p] = i
        return -1 if ans >= len(nums) else ans
