class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        course_map = {i: [] for i in range(numCourses)}
        degree = [0 for i in range(numCourses)]
        q = []
        counter = 0
        for c, p in prerequisites:
            course_map[c].append(p)
            degree[p] += 1

        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
                counter += 1
        while q:
            cur = q.pop(0)
            for p in course_map[cur]:
                degree[p] -= 1
                if degree[p] == 0:
                    q.append(p)
                    counter += 1

        return counter == numCourses
