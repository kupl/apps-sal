class Solution:
    def primeFactors(self, n):  # Prime factor decomposition
        out = set()
        while n % 2 == 0: 
            out.add(2)
            n //= 2
        for i in range(3, int(sqrt(n)) + 1, 2): 
            while n % i== 0: 
                out.add(i) 
                n //= i 
        if n > 2: 
            out.add(n)
        return out
    
    def largestComponentSize(self, A: List[int]) -> int:
        parents = [i for i in range(len(A))]
        size = [1] * len(A)
        primeIndexes = {}
        res = 0
        
        def find(target):
            curr = target
            
            while parents[curr] != curr:
                curr = parents[curr]
            
            return curr
        
        def union(a, b):
            aParent = find(a)
            bParent = find(b)
            
            if aParent == bParent:
                return
            
            size[aParent] += size[bParent]
            size[bParent] = 0
            parents[bParent] = aParent
            
        for idx, num in enumerate(A):
            factors = self.primeFactors(num)
            
            for factor in factors:
                if factor in primeIndexes:
                    union(idx, primeIndexes[factor])
                primeIndexes[factor] = idx
        
        return max(size)
