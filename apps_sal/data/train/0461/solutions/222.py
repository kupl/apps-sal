class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        res = 0
        graph = defaultdict(list)
        for index, parent in enumerate(manager):
            graph[parent].append(index)
        
        queue = deque([(headID, informTime[headID])])
        while queue:
            curId, curTime = queue.popleft()
            res = max(res, curTime)
            for child in graph[curId]:
                queue.append((child, curTime + informTime[child]))
        return res
        
        
        
        
        
        
        
#         rst = 0
#         childs = defaultdict(list)
#         for idx, parent in enumerate(manager):
#             childs[parent].append(idx)

#         q = deque([(headID, informTime[headID])])
#         while q:
#             cur_id, cur_time = q.popleft()
#             # calculate max
#             rst = max(rst, cur_time)
#             for child in childs[cur_id]:
#                 q.append((child, cur_time + informTime[child]))
#         return rst

