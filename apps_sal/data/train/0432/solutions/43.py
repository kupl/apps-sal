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
                for i in range(x+1,x+k):
                    if count[i] < val:
                        return False
                    count[i] -=1
            count[x] -=1
        return True
            

