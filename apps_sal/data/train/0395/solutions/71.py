class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        next_high = [0 for _ in range(len(A))]
        next_low = [0 for _ in range(len(A))]

        stack = []
        for val, i in sorted([(val, i) for i, val in enumerate(A)]):
            while stack and stack[-1] < i:
                next_high[stack.pop()] = i
            stack.append(i)

        stack = []
        for val, i in sorted([(-val, i) for i, val in enumerate(A)]):
            while stack and stack[-1] < i:
                next_low[stack.pop()] = i
            stack.append(i)

        dp = [[False for _ in range(len(A))] for _ in range(2)]
        dp[0][-1] = dp[1][-1] = True
        for i in range(len(A) - 2, -1, -1):
            dp[0][i] = dp[1][next_high[i]]
            dp[1][i] = dp[0][next_low[i]]

        return dp[0].count(1)
