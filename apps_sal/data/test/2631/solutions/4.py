class Solution:
     def canFinish(self, numCourses, prerequisites):
         """
         :type numCourses: int
         :type prerequisites: List[List[int]]
         :rtype: bool
         """
         graph = [[] for _ in range(numCourses)]
         visit = [0 for _ in range(numCourses)]
         for x, y in prerequisites:
             graph[x].append(y)
             
         ## states: 0 = unkonwn, 1 == visiting, 2 = visited
         def dfs(c,v):
             if v[c] == 2: return False
             if v[c] == 1: return True
             v[c]=1 #lable as visiting, if it does not visited eventually, it will cause an exception
             for i in graph[c]:
                 if dfs(i,v): return True
                 
             v[c]=2 # change to visited after done visiting
             return False
         
         
         for j in range(numCourses):
             if dfs(j,visit): return False
         return True
             

