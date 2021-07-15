class Solution:
   
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        if not str1 or not str2:
            return str1
        m, n = len(str1), len(str2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if str2[i-1] == str1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        #print(dp)
        final_str = ''
        i, j = n, m
        c1 = str1[j-1]
        c2 = str2[i-1]
        while i > 0 or j > 0:
            #print(f'{i} {c2} {j} {c1}')
            if c1 == c2:
                final_str += c1
                i -= 1
                j -= 1
                c1 = str1[j-1] if j > 0 else ''
                c2 = str2[i-1] if i > 0 else ''
            else:
                if i == 0 or dp[i][j-1] > dp[i-1][j]:
                    final_str += c1
                    j -= 1
                    c1 = str1[j-1] if j > 0 else ''
                else:
                    final_str += c2
                    i -= 1
                    c2 = str2[i-1] if i > 0 else ''
        return ''.join(reversed(final_str))
                    


