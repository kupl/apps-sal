class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        
        A.sort()
        A_set = set(A)
        cache = {}
        num_trees = 0
            
        # Update num trees. 
        for i, n in enumerate(A):
                        
            # Get factors pairs.
            factor_pairs = []
            for j in range(i):
                if n % A[j] == 0 and n // A[j] in A_set:
                    factor_pairs.append((n // A[j], A[j]))
                    
            # Compute num_trees.
            new_trees = 1
            for factor1, factor2 in factor_pairs:
                if factor1 != factor2:
                    new_trees += cache[factor1] * cache[factor2] # Each pair is run over twice. 
                elif factor1 == factor2:
                    new_trees += cache[factor1] * cache[factor2]
            num_trees += new_trees
            cache[n] = new_trees
            
        print(cache)    
        return num_trees % (10 ** 9 + 7)
