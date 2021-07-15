class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        
        count = {0:1}
        total = maxS = 0
        
        for num in A:
            total += num
            maxS += count.get(total-S,0)
            count[total] = count.get(total,0)+1

        return maxS
            

