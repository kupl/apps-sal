class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p
        if not remainder:
            return 0
        ans = float('inf')
        presum = [0]
        remainders = {0: -1}
        for (i, n) in enumerate(nums):
            presum.append(presum[-1] + n)
            r = ((cr := (presum[-1] % p)) - remainder) % p
            if r in remainders:
                ans = min(ans, i - remainders[r])
            remainders[cr] = i
        return ans if ans < len(nums) else -1
