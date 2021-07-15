class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # common factor as key, value stored in a set
        parents = list(range(max(A) + 1))
        
        def find(x):
            # find the parent/root of x 
            # does path compression simultaneously
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x
        
        def union(x, y):
            parents[find(x)] = parents[find(y)]
        
        for num in A:
            for k in range(2, int(sqrt(num)) + 1): 
                if num % k == 0:
                    union(num, k)
                    union(num, num//k)
        counts = {}
        maxC = 0
        for num in A:
            target = find(num)
            counts[target] = counts.get(target, 0) + 1
            maxC = max(maxC, counts[target])
            
        return maxC

