class Solution:

    def minOperations(self, nums: List[int]) -> int:
        hb = 0
        ans = 0
        for n in nums:
            for i in range(32):
                if n & 1 << i:
                    ans += 1
                    if i > hb:
                        hb = i
        return ans + hb
