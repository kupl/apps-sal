'''
n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]

'''


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(node):
            if not graph[node]:
                return 0
            else:
                max_time = 0
                for child in graph[node]:
                    max_time = max(max_time, dfs(child))
                return informTime[node] + max_time

        graph = collections.defaultdict(list)
        for i, j in enumerate(manager):
            graph[j].append(i)

        return dfs(headID)
