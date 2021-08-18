class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        '''
        Get prefix sum: pref[]
        Find the largest sorted list of indices index[] where
        pref[index[1]] - pref[index[0]] = pref[index[3]] - pref[index[2]] = ... = target
        '''
        pref = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pref[i + 1] = pref[i] + nums[i]

        d = {}
        ans = 0
        for i in range(len(pref)):
            if pref[i] - target in d:
                ans += 1
                d.clear()
            d[pref[i]] = i
        return ans
