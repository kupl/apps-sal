class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        relationships = {}

        for i in range(len(manager)):
            if not manager[i] in relationships:
                relationships[manager[i]] = [[], 0]
            relationships[manager[i]][0].append(i)

            if not i in relationships:
                relationships[i] = [[], 0]
            relationships[i][1] = informTime[i]

        def dfs(node, graph):
            if not graph[node][0]:
                return 0
            else:
                maxTime = 0
                informTime = graph[node][1]

                for nbr in graph[node][0]:
                    maxTime = max(maxTime, dfs(nbr, graph) + informTime)

                return maxTime

        return dfs(headID, relationships)
