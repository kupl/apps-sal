class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        sub = collections.defaultdict(list)
        for i,v in enumerate(manager):
            sub[v].append(i)
        res = -float('inf')
        def dfs(fa,time):
            nonlocal res
            if not sub[fa]: 
                res = max(res,time)
            else:
                for son in sub[fa]:
                    dfs(son,time+informTime[fa])
            return
        dfs(headID,0)
        return res if res < float('inf') else -1

