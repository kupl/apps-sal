from collections import *
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        mapper = defaultdict(list)
        for i, man in enumerate(manager):
            mapper[man].append(i)
        queue = [(headID,informTime[headID])]
        vis = set()
        ans = 0
        while queue:
            iden, time = queue.pop(0)
            ans = max(ans,time)
            vis.add(iden)
            for sub in mapper[iden]:
                if sub not in vis:
                    queue.append((sub, time + informTime[sub]))
        return ans
