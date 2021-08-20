class Solution:

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        N = numCourses
        O = [set() for _ in range(N)]
        for (b, a) in prerequisites:
            O[a].add(b)
        color = [0] * N

        def dfs(i):
            if color[i] == -1:
                return False
            elif color[i] == 1:
                return True
            color[i] = -1
            if any((not dfs(j) for j in O[i])):
                return False
            color[i] = 1
            return True
        return all(map(dfs, range(N)))
