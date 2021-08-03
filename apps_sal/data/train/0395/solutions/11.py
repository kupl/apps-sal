class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        next_large = [None] * n

        next_small = [None] * n

        arr1 = sorted([a, i] for i, a in enumerate(A))
        stack = []
        for a, i in arr1:
            while stack and stack[-1] < i:
                idx = stack.pop()
                next_large[idx] = i
            stack.append(i)
        arr2 = sorted([-a, i] for i, a in enumerate(A))
        stack = []
        for a, i in arr2:
            while stack and stack[-1] < i:
                idx = stack.pop()
                next_small[idx] = i
            stack.append(i)

        dp = [[None for _ in range(2)] for _ in range(n)]

        def dfs(i, is_odd):
            if i == n - 1:
                return True
            if dp[i][is_odd] is not None:
                return dp[i][is_odd]
            idx = next_large[i] if is_odd else next_small[i]
            if idx is None:
                dp[i][is_odd] = False
            else:
                dp[i][is_odd] = dfs(idx, is_odd ^ 1)
            return dp[i][is_odd]

        res = 0
        for i in range(n):
            if dfs(i, 1):
                res += 1
        return res
