class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        
        
        ans = 0
        count = [0, 0]
        max_count = 0
        l = 0
        for r in range(len(A)):
            # update the count
            count[A[r]] += 1
            max_count = max(max_count, count[1])
            if r - l + 1 - max_count > K:
                count[A[l]] -= 1
                l += 1
            else:
                ans = max(ans, r - l + 1)
        
        return ans
            

