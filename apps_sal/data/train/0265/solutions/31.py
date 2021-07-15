class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        pref = {}
        pref[0] = -1
        ans = 0
        presum = 0
        j = -1
        for i in range(len(nums)):
            presum += nums[i]
            c = presum - target
            if c in pref and pref[c] >= j:
                ans += 1
                j = i
            pref[presum] = j
        return ans

