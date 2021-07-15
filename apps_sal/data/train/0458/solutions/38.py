class Solution:
    def minSubarray(self, nums: List[int], K: int) -> int:
        P = [0]
        for x in nums:
            P.append((P[-1]+x)%K)
        ans = len(nums)
        last = {}
        for j,q in enumerate(P):
            last[q] = j
            p = (q-P[-1])%K
            if p in last:
                ans = min(ans,j-last[p])
        return ans if ans < len(nums) else -1
        
        

