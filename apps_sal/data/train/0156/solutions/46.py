class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # build dp for LCS
        dp = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
        
        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                diag = dp[r-1][c-1]
                up = dp[r-1][c]
                left = dp[r][c-1]
                if str1[c-1] == str2[r-1]:
                    diag += 1
                dp[r][c] = max(diag, up, left)
        
        # build supersequence by going up the dp grid
        r = len(str2)
        c = len(str1)
        res = []
        while r > 0 and c > 0:
            if str1[c-1] == str2[r-1]:
                res.append(str1[c-1])
                r -= 1
                c -= 1
            else:
                # move up/left depending on which dp is larger
                up = dp[r-1][c]
                left = dp[r][c-1]
                if up > left:
                    # move up
                    res.append(str2[r-1])
                    r -= 1
                else:
                    # move left
                    res.append(str1[c-1])
                    c -= 1
        
        while r > 0:
            res.append(str2[r-1])
            r -= 1
        
        while c > 0:
            res.append(str1[c-1])
            c -= 1
        
        return ''.join(res[::-1])
