class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for i in range(n)]
        for i, m in enumerate(manager):
            if m >= 0:
                children[m].append(i)

        def dfs(i):
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
        return dfs(headID)
        # subordinates = [[] for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         if manager[j] == i:
        #             subordinates[i].append(j)
        # res = [0] * n
#         # print(subordinates)l
#         def helper(id, current_time):
#             time = informTime[id] + current_time
#             subs = subordinates[id]
#             if subs:
#                 for k in subs: helper(k, time)
#             else:
#                 res[id] = time

#         helper(headID, 0)
#         return max(res)
#         queue = deque([(manager.index(-1), 0)])
#         while queue:
#             i, t = queue.popleft()
#             for j in subordinates[i]:
#                 res[j] = t
#                 queue.append((j, t + informTime[i]))
#         return max(res)
