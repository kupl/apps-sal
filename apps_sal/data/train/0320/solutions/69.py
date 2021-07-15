class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        maxt = 0
        for i in nums:
            if i == 0: continue
            t = 0
            while i > 0:
                if i & 1:
                    i -= 1
                    ans += 1
                else:
                    i >>= 1
                    t += 1
            maxt = max(maxt, t)
        ans += maxt
        return ans
