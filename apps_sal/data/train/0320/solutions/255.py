import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return sum( bin(x).count('1') for x in nums ) + max(len(bin(x)) for x in nums ) - 3
            
                
        
        

