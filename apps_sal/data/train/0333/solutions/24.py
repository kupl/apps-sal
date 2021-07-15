class Solution:
    def minJumps(self, arr: List[int]) -> int:

        
        # Each array index is a node
        # Each link (i+1), (i-1), (arr[i] == arr[j]) is a connection
        # Create a graph of arr
        # BFS to find the shortest path from 0 to arr.length - 1
        
        if len(arr) == 1: return 0
        
        val_to_id = collections.defaultdict(set)
        id_to_neigh = {}
        
        for i,val in enumerate(arr):
            if (not i) or (i == len(arr) - 1):
                val_to_id[val].add(i)
            elif not (arr[i-1] == arr[i] == arr[i+1]):
                val_to_id[val].add(i)
        
        for i,val in enumerate(arr):
            if (not i) or (i == len(arr) - 1):
                id_to_neigh[i] = set([i-1,i+1])|val_to_id[val]
                id_to_neigh[i] -= set([-1, len(arr), i])
            elif not (arr[i-1] == arr[i] == arr[i+1]):
                id_to_neigh[i] = set([i-1,i+1])|val_to_id[val]
                id_to_neigh[i].remove(i)
                
        t = len(arr) - 1 # target index
        q = [(0, 0)] # (n) number of jumps, (i) current index
        v = set([0])

        while q:
            
            level = []
            
            for n, i in q:
                if i == t:
                    return n
                for j in id_to_neigh.get(i, []):
                    if j not in v:
                        v.add(j)
                        level.append((n+1, j))
            q = level
