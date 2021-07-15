class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # dp[i][k]: minimum cost to make s[:i] can be divided into k substring
        # xxxxxxxxxxxxxjxxxxxxi
        # dp[j-1][k-1]  s[j:i] 
        n = len(s)
        dp = [[math.inf for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0] = 0
        
        def changes(start, end):
            cnt = 0
            while start < end:
                if s[start] != s[end]:
                    cnt += 1
                start += 1
                end -= 1
            return cnt
        
        for i in range(1, n + 1):
            for l in range(1, min(k, i) + 1):
                for j in range(l, i + 1):
                    dp[i][l] = min(dp[i][l], dp[j - 1][l - 1] + changes(j - 1, i - 1))
        
        return dp[n][k]

