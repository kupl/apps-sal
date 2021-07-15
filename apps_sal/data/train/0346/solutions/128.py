class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        l, r, oddsCounter, res = 0, 0, 0, 0
        while r < len(nums):
            if nums[r] % 2 == 1:
                oddsCounter += 1
            while oddsCounter >k:
                if nums[l] % 2 == 1:
                    oddsCounter -= 1
                l += 1
            if oddsCounter == k: 
                res += 1 
            i = l
            while oddsCounter == k and i<r and nums[i]%2 == 0:
                res += 1
                i += 1
            r += 1   

        return res
