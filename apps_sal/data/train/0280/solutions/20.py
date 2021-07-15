class Solution:
    def palindromePartition(self, s: str, k: int):
        prefix = [[0] * len(s) for _ in range(len(s))]
        for r in range(len(prefix)):
            for c in range(len(prefix[0])):
                if r < c:
                    prefix[r][c] = self.find_change(s, r, c)

        dp = [[0] * len(s) for _ in range(k)]
        dp[0] = prefix[0]
        for r in range(1, len(dp)):
            for c in range(len(dp[0])):
                if r < c:
                    tmp = float('inf')
                    for i in range(c):
                        tmp = min(tmp, dp[r-1][i] + prefix[i+1][c])
                    dp[r][c] = tmp
        return dp[-1][-1]

    def find_change(self, s, r, c):
        res = 0
        while r < c:
            if s[r] != s[c]:
                res += 1
            r += 1
            c -= 1
        return res
