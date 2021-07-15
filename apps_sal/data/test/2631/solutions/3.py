class Solution:
     def canFinish(self, numCourses, prerequisites):
         """
         :type numCourses: int
         :type prerequisites: List[List[int]]
         :rtype: bool
         """
         pre_count = [0] * numCourses
         next_courses = [[] for _ in range(numCourses)]
         
         for cur, pre in prerequisites:
             next_courses[pre].append(cur)
             pre_count[cur] += 1
         
         q = []
         
         # always chose courses without prereq
         for i, count in enumerate(pre_count):
             if count == 0:
                 q.append(i)
         
         finish_num = 0
         # take those courses which can be taken after finishing prereq
         while q:
             course = q.pop(0)
             finish_num += 1
             for next_course in next_courses[course]:
                 pre_count[next_course] -= 1
                 if pre_count[next_course]  == 0:
                     q.append(next_course)
         
         return finish_num == numCourses
             
         

