from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) %k != 0 or len(nums) == 0: return False
        
        count = Counter(nums)
        
        nums = sorted(nums)
        for x in nums:
            if count[x] == 0:
                continue
            else:
                val = count[x]
                for i in range(x,x+k):
                    count[i] -= val
                    if count[i] < 0:
                        return False
                    
        return True
            

