from collections import defaultdict

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        max_time = 0
        n = len(arr)
        
        curr = [0 for _ in range(n)]
        
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        
        size_tracker = defaultdict(lambda: 0)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y, time):
            xs, ys = find(x), find(y)
            if xs == ys: return False
            if size[xs] < size[ys]:
                xs, ys = ys, xs
            size_tracker[size[xs]] -= 1
            size_tracker[size[ys]] -= 1
            size[xs] += size[ys]
            size_tracker[size[xs]] += 1
            if size_tracker[m] > 0: max_time = time + 1
            parent[ys] = xs
            return True
        
        for t in range(n):
            x = arr[t] - 1
            curr[x] = 1
            size_tracker[1] += 1
            if x > 0 and curr[x-1] == 1:
                union(x, x-1, t)
            if x < len(curr)-1 and curr[x+1] == 1:
                union(x, x+1, t)
            if size_tracker[m] > 0:
                max_time = t + 1
                
        return max_time if max_time > 0 else -1
        
        
        
            
            
            
            

