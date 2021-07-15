class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        
        parent = [-1]*100001
        
        def find(x , parent) :
            if parent[x] == -1 :
                return x
            
            parent[x] = find(parent[x] , parent)
            
            return parent[x]
        
        def union(x , y ) :
            xp = find(x , parent)
            yp = find(y , parent)
            
            if xp != yp :
                parent[yp] = xp
                
        for i in range(len(A)) :
            for j in range(2 , int(sqrt(A[i])) + 1) :
                
                if A[i] % j == 0 :
                    union(j , A[i])
                    union(A[i] , A[i] //j)
                    
        count = 0 
        cache = {}
        
        for x in A :
            p = find(x , parent) 
            count = max(count , 1 + cache.get(p , 0 ))
            
            cache[p] = cache.get(p , 0) + 1
            
        return count

