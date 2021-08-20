class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        report = collections.defaultdict(list)
        for (idx, i) in enumerate(manager):
            report[i].append(idx)
        queue = [(headID, informTime[headID])]
        maxT = 0
        while queue:
            (n, t) = queue.pop(0)
            maxT = max(maxT, t)
            for r in report[n]:
                queue.append((r, t + informTime[r]))
        return maxT
