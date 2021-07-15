class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s = set(A)
        ans = 0
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                x,y = A[i],A[j]
                l = 2
                while x+y in s:
                    x,y = y,x+y
                    l += 1
                ans = max(ans,l)
        return ans if ans >= 3 else 0

