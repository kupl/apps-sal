from collections import defaultdict


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        companyTree = defaultdict(list)
        for (idx, head) in enumerate(manager):
            if head != -1:
                companyTree[head].append(idx)
        queue = deque([(headID, 0)])
        visited = set()
        res = 0
        while queue and len(visited) < n:
            (cur_employee, cur_total) = queue.popleft()
            res = max(res, cur_total + informTime[cur_employee])
            for subord in companyTree[cur_employee]:
                queue.append((subord, cur_total + informTime[cur_employee]))
        return res
