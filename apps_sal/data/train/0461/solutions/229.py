class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        d = collections.defaultdict(list)
        for i in range(n):
            d[ manager[i] ].append(i)
        
        res = 0
        que = collections.deque( [ [ d[-1][0], 0 ] ] )
        
        while que:
            cur, time = que.popleft()
            res = max(res, time)
            time += informTime[cur]
            
            for t in d[cur]:
                que.append( [t, time] )
        
        return res
        

