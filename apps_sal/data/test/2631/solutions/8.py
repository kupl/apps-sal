class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque

        class Vertex(object):
            def __init__(self):
                self.inDegree = 0
                self.visited = False
                self.adjList = []
                self.invAdjList = []

            def info(self):
                print(self.adjList)
                print(self.invAdjList, self.inDegree)
                print(self.visited)
        vertices = []
        for _ in range(numCourses):
            vertices.append(Vertex())

        for i in prerequisites:
            pre = i[0]
            post = i[1]
            vertices[pre].adjList.append(post)
            vertices[post].inDegree += 1
            vertices[post].invAdjList.append(pre)

        q = deque()
        coursesLearned = []
        for i in range(numCourses):
            if vertices[i].inDegree == 0:
                q.append(i)

        while q:
            course = q.popleft()
            coursesLearned.append(course)
            vertices[course].visited = True
            for c2 in vertices[course].adjList:
                vertices[c2].inDegree -= 1
                if vertices[c2].inDegree == 0:
                    q.append(c2)
        return len(coursesLearned) == numCourses
