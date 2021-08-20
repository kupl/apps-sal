class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        bns = 0
        for x in nums:
            b = bin(x)
            ans += b.count('1')
            if x:
                bns = max(bns, len(b) - 2)
        return ans + max(bns - 1, 0)
