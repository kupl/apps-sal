class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:

        A.sort()
        self.ans = 0

        def check(A, i, path):
            return int((A[i] + path[-1])**0.5 + 0.0)**2 == A[i] + path[-1]

        def dfs(A, path):
            if len(A) == 0:
                self.ans += 1
                return

            for i in range(len(A)):
                if i > 0 and A[i] == A[i - 1]:
                    continue
                if len(path) == 0 or (len(path) > 0 and check(A, i, path)):
                    dfs(A[:i] + A[i + 1:], path + [A[i]])

        dfs(A, [])
        return self.ans
