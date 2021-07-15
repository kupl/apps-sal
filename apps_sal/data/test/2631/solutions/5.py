class Solution:
     def canFinish(self, numCourses, prerequisites):
         """
         :type numCourses: int
         :type prerequisites: List[List[int]]
         :rtype: bool
         """       
         in_degrees = collections.defaultdict(int)        
         edges = collections.defaultdict(list)
 
         for i in range(0, numCourses):
             in_degrees[i] = 0            
         
         for prerequisty in prerequisites:
             start = prerequisty[1]
             end = prerequisty[0]
             edges[start].append(end)
             in_degrees[end] += 1
 
         queue = collections.deque()
         
         for i in range(0, numCourses):
             if in_degrees[i] == 0:
                 queue.append(i)
             
         count = 0
         while len(queue) > 0:
             node = queue.popleft()
             count += 1
             
             for neighbor in edges[node]:
                 in_degrees[neighbor] -= 1
                 if in_degrees[neighbor] == 0:
                     queue.append(neighbor)
                     
         return count == numCourses        
