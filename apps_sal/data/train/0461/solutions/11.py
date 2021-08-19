class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        #           headID
        #         /        \\
        #      sub1         sub2
        #      / \\          / \\
        #   sub11 sub12  sub21 sub22

        subs = [[] for i in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                subs[m].append(i)

        def my_dfs(root):

            if subs[root] is None:
                return informTime[root]

            return max([my_dfs(s) for s in subs[root]] or [0]) + informTime[root]

        return my_dfs(headID)


#     def numOfMinutes(self, n, headID, manager, informTime):
#         children = [[] for i in xrange(n)]
#         for i, m in enumerate(manager):
#             if m >= 0: children[m].append(i)

#         def dfs(i):
#             return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
#         return dfs(headID)

    # def dfs(i):
    #         if manager[i] != -1:
    #             informTime[i] += dfs(manager[i])
    #             manager[i] = -1
    #         return informTime[i]
    #     return max(map(dfs, range(n)))
