class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # Compress the array:
        # for any sub array s[i] == s[i+1] == s[i+2]... we only care about the start and the end        
        arr = [x for i, x in enumerate(arr) if i == 0 or i == len(arr)-1 or x != arr[i-1] or x != arr[i+1]]
        
        d = {}
        # O(N)
        for i, x in enumerate(arr):
            d.setdefault(x, set()).add(i)
        # Build graph O(N^2)
        adj = {}
        for i, x in enumerate(arr):
            adj[i] = set()
            if i != 0: adj[i].add(i-1)
            if i != len(arr)-1: adj[i].add(i+1)
            adj[i] |= d[arr[i]] # O(N^2)?
            adj[i].remove(i)
            
        #print(adj)
        # BFS
        q = collections.deque()
        distance = [len(arr)-1] * len(arr)
        q.append(0)
        count = 0
        while q:
            nxt_q = collections.deque()
            while q:
                nxt = q.popleft()
                if distance[nxt] <= count: continue
                distance[nxt] = count
                for x in adj[nxt]:
                    nxt_q.append(x)
            q = nxt_q
            count += 1
        return distance[-1]

