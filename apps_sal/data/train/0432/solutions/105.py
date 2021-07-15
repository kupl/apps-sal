from collections import Counter

class Solution:
    '''
    Good use of counter
    Same can be done in complex way with sorting the array and using orderedDict
    '''
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        while c:
            m = min(c)
            for i in range(m, m+k):
                if i not in c:
                    return False
                elif c[i] == 1:
                    del c[i]
                else:
                    c[i] -= 1
                    
        return True
                

