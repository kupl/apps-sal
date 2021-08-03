class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        visited = [False] * n
        res = []
        self.count = 0

        def dfs(curr):
            if len(curr) == n:
                self.count += 1
                return
            for i in range(n):
                if visited[i]:
                    continue
                if i > 0 and A[i] == A[i - 1] and not visited[i - 1]:
                    continue
                if len(curr) > 0 and (int((curr[-1] + A[i]) ** 0.5))**2 != curr[-1] + A[i]:
                    continue
                visited[i] = True
                dfs(curr + [A[i]])
                visited[i] = False
        dfs([])
        return self.count
