
  
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        n = len(A)
        tips = sorted(A)
        
        
        index = { x: i for i, x in enumerate(tips) }
        d = [1] * n
        
        for i, x in enumerate(tips):
            head = x

            for j in range(i):
                x = tips[j]
                
                y = head // x
                
                if y*x != head:
                    continue
                if y in index:
                    leaf_1 = j
                    leaf_2 = index[y]
                    d[i] = d[i] + (d[leaf_1] * d[leaf_2])
                    
        return sum(d) % MOD
