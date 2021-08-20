class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if len(A) > len(B):
            return self.maxUncrossedLines(B, A)
        if not A or not B:
            return 0
        dp = [[0] * len(B) for _ in range(len(A))]
        indexB = collections.defaultdict(list)
        for (i, num) in enumerate(B):
            indexB[num].append(i)
        for i in reversed(list(range(len(A)))):
            for j in reversed(list(range(len(B)))):
                found = False
                for idx in indexB.get(A[i], []):
                    if idx >= j:
                        found = True
                        break
                if found:
                    dp[i][j] = max(1 + (dp[i + 1][idx + 1] if i + 1 < len(A) and idx + 1 < len(B) else 0), dp[i + 1][j] if i + 1 < len(A) else 0)
                else:
                    dp[i][j] = dp[i + 1][j] if i + 1 < len(A) else 0
        return dp[0][0]
