class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n <= 1:
            return 0
        rst = 0
        childs = defaultdict(list)
        for (idx, parent) in enumerate(manager):
            childs[parent].append(idx)
        queue = deque([(headID, informTime[headID])])
        while queue:
            (cur_id, cur_time) = queue.popleft()
            rst = max(rst, cur_time)
            for child in childs[cur_id]:
                queue.append((child, cur_time + informTime[child]))
        return rst
