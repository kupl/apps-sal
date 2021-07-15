class Solution:
     def canFinish(self, numCourses, prerequisites):
         """
         :type numCourses: int
         :type prerequisites: List[List[int]]
         :rtype: bool
         """
         
         N = numCourses
         
 #         # sol1: topo sort
 #         indegree = [0] * N
         O = [set() for _ in range(N)]
         for b, a in prerequisites:
             O[a].add(b)
 #             indegree[b] += 1
             
 #         q = [c for c in range(N) if indegree[c] == 0]
 #         done = 0
 #         while q:
 #             c = q.pop()
 #             done += 1
 #             for post in O[c]:
 #                 indegree[post] -= 1
 #                 if indegree[post] == 0:
 #                     q.append(post)
 #         return done == N # CAUTION
         
         # sol2: dfs
         color = [0] * N
         def dfs(i):
             if color[i] == -1:
                 return False
             elif color[i] == 1:
                 return True
             color[i] = -1
             if any(not dfs(j) for j in O[i]):
                 return False
             color[i] = 1
             return True
         
         return all(map(dfs, range(N)))
