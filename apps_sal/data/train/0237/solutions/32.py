class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        size = len(A)
        prefix = {0: 1}
        cnt = 0
        ans = 0
        
        for i, num in enumerate(A):
            if num == 1: cnt += 1
            if cnt - S in prefix:
                ans += prefix[cnt-S]
            prefix[cnt] = prefix.get(cnt, 0) + 1
        
        return ans
