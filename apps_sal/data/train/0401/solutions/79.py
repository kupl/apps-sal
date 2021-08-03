class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        seen = [0] * 3
        for a in nums:
            for i in seen[:]:
                seen[(i + a) % 3] = max(seen[(i + a) % 3], i + a)
        return seen[0]

        '''
        3,6,5,1,8

        0 , 0 , 0 
        
        
        '''
