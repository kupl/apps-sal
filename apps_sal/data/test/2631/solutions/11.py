class Solution:

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = {i: [] for i in range(numCourses)}
        degree = [0 for i in range(numCourses)]
        for (k, v) in prerequisites:
            edges[v].append(k)
            degree[k] += 1
        q = []
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        count = 0
        while q:
            node = q.pop()
            count += 1
            for nn in edges[node]:
                degree[nn] -= 1
                if degree[nn] == 0:
                    q.append(nn)
        return count == numCourses
