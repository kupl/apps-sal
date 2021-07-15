from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        
        while count:
            minimum = min(count)
            for i in range(minimum,minimum+k):
                if i not in count:
                    return False
                else:
                    if count[i] == 1:
                        del count[i]
                    else:
                        count[i] -= 1
                        
        return True
    
# As the description says question is same as 846
# Difference with 659 is that it has to be exactly K instead of atleast K

