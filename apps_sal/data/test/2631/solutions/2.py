class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        N = numCourses
        indegree = [0] * N
        O = [set() for _ in range(N)]
        for b, a in prerequisites:
            O[a].add(b)
            indegree[b] += 1

        stack = [c for c in range(N) if indegree[c] == 0]
        done = 0
        while stack:
            i = stack.pop()
            done += 1
            for j in O[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    stack.append(j)
        return done == N
