class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        G = collections.defaultdict(list)
        for i,v in enumerate(manager):
            G[v].append(i)
        
        ans = 0
        
        qu = [(G[-1][0], 0)]
        while qu:
            n, v = qu.pop()
            ans = max(ans,v)
            for e in G[n]:
                qu.append((e, v+informTime[n]))
        return ans
