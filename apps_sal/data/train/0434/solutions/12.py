class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = -1
        k = 1
        maxi = 0
        count = 0
        i = 0
        while i != len(nums):
            if nums[i] == 0:
                if k == 0:
                    i = zero + 1
                    zero = i
                    maxi = max(count, maxi)
                    count = 0
                    k = 1
                else:
                    k -= 1
                    zero = i
                    i += 1                    
            else:
                count += 1
                i += 1
        maxi = max(count, maxi)
        if maxi == len(nums):
            return maxi - 1
        else:
            return maxi
