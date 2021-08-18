class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        import math
        curr_gcd = nums[0]
        for i in range(1, len(nums)):
            curr_gcd = math.gcd(curr_gcd, nums[i])
            if curr_gcd == 1:
                return True
        return curr_gcd == 1

        '''
        29, 6, 10
        29, 3*2, 5*2
        '''
