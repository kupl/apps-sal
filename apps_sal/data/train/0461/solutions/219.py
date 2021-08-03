from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # DFS Stack
        self.max = 0
        directSub = self.makeDirectSub(n, manager)
        self.dfs(headID, directSub, informTime)
        return self.max

    # def makeDirectSub(self, n, manager):
    #     d = {employee: [] for employee in range(n)}
    #     for employee in range(len(manager)):
    #         if manager[employee] != -1:
    #             d[manager[employee]].append(employee)
    #     return d

    def makeDirectSub(self, n, manager):
        d = defaultdict(list)
        for sub, employee in enumerate(manager):
            d[employee].append(sub)
        return d

    def dfs(self, headID, directSub, informTime):
        stk = [(headID, 0)]
        while stk:
            employee, time = stk.pop()
            self.max = max(self.max, time)
            # add all subemployees and record the time it took them to get the information
            for subEmp in directSub[employee]:
                stk.append((subEmp, time + informTime[employee]))
        return


# from collections import deque, defaultdict

# class Solution(object):
#     def numOfMinutes(self, n, headID, manager, informTime):
#         \"\"\"
#         :type n: int
#         :type headID: int
#         :type manager: List[int]
#         :type informTime: List[int]
#         :rtype: int
#         \"\"\"
#         if n <= 1:
#             return 0
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
