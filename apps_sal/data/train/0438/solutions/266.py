class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        from collections import defaultdict 
        parents = [i for i in range(n)]
        ranks = [0] * n
        size = [1] * n 
        group_size = [0] * (n+1)
        visited = [False] * n
        
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            r1 = find(x)
            r2 = find(y)
         
            if r1 != r2:
                group_size[size[r1]] -= 1 
                group_size[size[r2]] -= 1 
                size[r1] = size[r2] = size[r1] + size[r2]
                group_size[size[r1]] += 1 
            
                if ranks[r2] > ranks[r1]:
                    r1, r2 = r2, r1 
                
                parents[r2] = r1 
                if ranks[r1] == ranks[r2]:
                    ranks[r1] += 1
        
        ans = -1
        for step, idx in enumerate(arr):
            idx -= 1 
            left, right = idx - 1, idx + 1
            group_size[1] += 1 
            if left >= 0 and visited[left]:
                union(idx, left)
            if right < n  and visited[right]:
                union(idx, right)
            
            visited[idx] = True
            if group_size[m] > 0:
                ans = step + 1 
        
        return ans
