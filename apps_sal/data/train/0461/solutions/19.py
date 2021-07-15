class Solution:
    def build_graph(self,n,manager,informTime,headID):
        
        graph={x:[] for x in range(n)}
        
        for i in range(n):

            mgr=manager[i]
            emp=i
            
            if mgr == -1: continue
            
            if graph.get(mgr,0):
                graph[mgr].append(emp)
            else:
                graph[mgr]=[emp]
        
        return graph
    def traverse_graph(self, graph, headID, informTime):
        result=0
        
        for v in graph[headID]:
            result = max(result, self.traverse_graph(graph, v, informTime));
        
        return result+informTime[headID]
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph=self.build_graph(n,manager,informTime, headID)
        return self.traverse_graph(graph, headID, informTime)
