class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        set_a = set(A)        
        seen = set()
        
        n = len(A)
        last = A[-1]
        
        g = 0
        
        def dfs(x, y):
            seen.add((x, y))
            if (z := x + y) in set_a:
                return 1 + dfs(y, z)
            else:
                return 0
              
        for i in range(n - 1):
            for j in range(i + 1, n):
                if A[i] + A[j] > last:
                    break
                if (A[i], A[j]) in seen:
                    continue
                g = max(g, dfs(A[i], A[j]))
                
                
                
                
        return g + 2 if g else 0      
