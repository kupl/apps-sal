class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        longest = 0
        neg = len(nums)
        pos = -1
        
        prod = 1
        for i, n in enumerate(nums):
            if not n:
                neg = len(nums) 
                pos = i
                prod = 1
            else:
                prod *= n
                
                if prod < 0:
                    neg = min(neg, i)
                    longest = max(longest, i - neg)
                else:
                    longest = max(longest, i - pos)
            
        return longest
