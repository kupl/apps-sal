class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T: return 0
        
        b2b = collections.defaultdict(list)
        s2b = collections.defaultdict(list)
        for i in range(len(routes)):
            for s in routes[i]: s2b[s].append(i)
            for j in range(i+1, len(routes)):
                if set(routes[i]) & set(routes[j]):
                    b2b[i].append(j)
                    b2b[j].append(i)
                    
        q = collections.deque([[b, 1] for b in s2b[S]])
        seen = set()
        while q:
            b, lvl = q.popleft()
            if b in seen: continue
            seen.add(b)
            if T in routes[b]: return lvl
            for b2 in b2b[b]: 
                if b2 not in seen: q.append([b2, lvl+1])
        return -1
