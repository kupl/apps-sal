class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # using manager make graph => Value is key, Index is value, cost is informTime[Value]
# do DFS find max
        
        graph = []
        for i in range(n):
            graph.append([])
        for i in range(len(manager)):
            if(manager[i]!=-1):
                graph[manager[i]].append(i)
        print(graph)
        # DFS
        stack =[(headID, 0)]
        cost =0
        maxi =0
        while(len(stack)):
            node, cost = stack.pop()
            cost += informTime[node]
            if(cost>maxi):
                maxi = cost
            for child in graph[node]:
                stack.append((child, cost))
        return maxi

