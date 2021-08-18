class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        N = numCourses

        O = [set() for _ in range(N)]
        for b, a in prerequisites:
            O[a].add(b)
        visit = [0] * N

        def dfs(i):
            if visit[i] == -1:
                return False
            elif visit[i] == 1:
                return True

            visit[i] = -1
            if any(not dfs(j) for j in O[i]):
                return False
            visit[i] = 1
            return True

        return all(map(dfs, range(N)))
