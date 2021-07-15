class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        count, n, l = 0, len(A), 0
        ans = 0
        for r in range(n):
            count += 1 - A[r]
            while count > K:
                count -= 1 - A[l]
                l += 1
            ans = max(ans, r-l+1)
        return ans
            

