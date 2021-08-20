class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        rst = 0
        childs = defaultdict(list)
        for (idx, parent) in enumerate(manager):
            childs[parent].append(idx)
        q = deque([(headID, informTime[headID])])
        while q:
            (cur_id, cur_time) = q.popleft()
            rst = max(rst, cur_time)
            for child in childs[cur_id]:
                q.append((child, cur_time + informTime[child]))
        return rst
