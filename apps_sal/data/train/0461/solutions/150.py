class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        # DFS

        subordinates = collections.defaultdict(list)

        for i, m in enumerate(manager):

            if i != headID:
                subordinates.setdefault(m, []).append(i)
                # subordinates[m].append(i)

        self.res = 0

        def dfs(manager, time):

            self.res = max(self.res, time)

            for subordinate in subordinates[manager]:

                dfs(subordinate, time + informTime[manager])

        dfs(headID, 0)

        return self.res
