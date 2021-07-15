class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op0 = sum(bin(num).count('1') for num in nums)
        op1 = len(bin(max(nums))) - 3
        return op0 + op1
            
                    
            

