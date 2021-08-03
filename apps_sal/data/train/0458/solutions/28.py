class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_sum = list(accumulate(nums))
        target = prefix_sum[-1] % p

        if target == 0:
            return 0

        d = defaultdict(lambda: -1)
        ans = float('inf')

        for i, ps in enumerate(prefix_sum):
            if i < len(nums) - 1 and ps % p == target:
                ans = min(ans, i + 1)
            if d[ps % p] != -1:
                ans = min(ans, i - d[ps % p])
            d[(target + ps % p) % p] = i

        return ans if ans != float('inf') else -1
