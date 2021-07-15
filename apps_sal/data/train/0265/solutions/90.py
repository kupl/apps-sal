class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        pos = {0: 0}
        cumsum = 0
        ans = 0
        
        for num in nums:
            cumsum += num
            pos[cumsum] = max(ans, pos.get(cumsum-target, -1)+1)
            ans = max(ans, pos[cumsum])
            #print(pos, cumsum)
        return ans

