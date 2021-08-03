class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        changes = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(i, len(s)):
                start, end = i, j
                tmp = 0
                while start < end:
                    if s[start] != s[end]:
                        tmp += 1
                    start += 1
                    end -= 1
                changes[i][j] = tmp

        memo = [[float('inf')] * len(s) for _ in range(k)]

        for i in range(len(s)):
            memo[0][i] = changes[i][-1]

        for i in range(1, k):
            for j in range(len(s)):
                for t in range(j + 1, len(s) - i + 1):
                    memo[i][j] = min(memo[i - 1][t] + changes[j][t - 1], memo[i][j])

        return memo[-1][0]
