from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index_map = { x:i for i, x in enumerate(A) }
        longest = defaultdict(lambda: 2)
        ans = 0
        
        for k in range(len(A)):
            for j in range(len(A)):
                target = A[k] - A[j]
                i = index_map.get(target, -1)
                
                if i >= 0 and i < j:
                    cand = longest[j,k] = longest[i,j] + 1
                    ans = max(ans, cand)
        
        return ans
         

