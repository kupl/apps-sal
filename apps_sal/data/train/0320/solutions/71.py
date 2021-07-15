class Solution:
    def minOperations(self, nums: List[int]) -> int:
        doubles = 0
        incs = 0
        
        for num in nums:
            numDoubles = 0
            while num > 0:
                if num%2 == 0:
                    num //= 2
                    numDoubles += 1
                else:
                    num -= 1
                    incs += 1
            doubles = max(doubles, numDoubles)
        
    
        return doubles + incs
