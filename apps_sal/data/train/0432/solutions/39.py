class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        
        while count:
            minCount = min(count)
            
            for i in range(minCount, minCount+k):
                if not count[i]:
                    return False
                if count[i] == 1:
                    del count[i]
                else:
                    count[i] -= 1
        return True
