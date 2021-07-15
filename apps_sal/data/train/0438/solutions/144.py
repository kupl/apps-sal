class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        
        def find(u):
            if parent[u] == u:
                return u
            else:
                parent[u] = find(parent[u])
                return parent[u]
            
        def union(u,v):
            pu = find(u)
            pv = find(v)
            
            if pv!=pu:
                store[size[pv]]-=1
                store[size[pu]]-=1
                size[pu] += size[pv]
                size[pv] = 0
                store[size[pu]]+=1
                parent[pv] = pu
                
            return size[pu]
                
                
        
        n = len(arr)
        
        parent = [0]*n ;size = [0]*n;val = [0]*n
        store = defaultdict(int)
        
        for i in range(n):
            arr[i]-=1
            parent[i] = i
        
        ans = -1
        for i in range(n):
            size[arr[i]] =1
            val[arr[i]] = 1
            store[1]+=1
            curr = 0
            
            if arr[i] - 1 >= 0 and val[arr[i]-1] == 1:
                curr = union(arr[i],arr[i]-1)
                
            if arr[i]+1 < n and val[arr[i]+1] == 1:
                curr = union(arr[i],arr[i]+1)
                
            if store[m] > 0:
                ans = i+1
                
        
        return ans

