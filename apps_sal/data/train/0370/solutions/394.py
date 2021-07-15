class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n=len(A)
        parent=[i for i in range(max(A)+1)]
        
        def find(x):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        
        def union(x, y):
            px=find(x)
            py=find(y)
            if px==py:
                return px
            parent[py]=px
            return px
        
        
        for a in A:
            for k in range(2, int(sqrt(a))+1, 1):
                if a%k==0:
                    union(a, k)
                    union(a, a//k)
        max_len=0 
        d=defaultdict(int)
        for a in A:
            group_id = find(a)
            d[group_id]+=1
            max_len = max(max_len, d[group_id])
        return max_len
            
                
                    
                

