class Solution:
    def canFinish(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def ok(node):
            if seens[node] == -1:
                return False
            if not seens[node]:
                seens[node] = -1
                for pre in pres[node]:
                    if not ok(pre):
                        return False
                seens[node] = 1
            return True

        pres = [[] for _ in range(n)]
        for cur, pre in prerequisites:
            pres[cur].append(pre)

        seens = [0] * n
        for node in range(n):
            if not ok(node):
                return False
        return True
