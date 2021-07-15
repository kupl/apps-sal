class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        dp = [[0 for _ in range(len(mat[0]) + 1)]for r in range(len(mat) + 1)]
        
        for r in range(1, len(mat) + 1):
            for c in range(1, len(mat[r-1]) + 1):
                dp[r][c] += mat[r-1][c-1]
                if not r and not c:
                    continue
                elif not r:
                    dp[r][c] += dp[r][c-1]
                    continue
                elif not c:
                    dp[r][c] += dp[r-1][c]
                    continue
                dp[r][c] += dp[r][c-1] + dp[r-1][c] - dp[r-1][c-1]
         
        # print(dp)
        highest = -1
        for r in range(1, len(dp)):
            r0= r1 = r
            c0= c1 = 1
            while r1 < len(dp) and c1 < len(dp[0]):
              
                result = dp[r1][c1] + dp[r0-1][c0-1] - dp[r1][c0-1] - dp[r0-1][c1]
  
                # print(f'r0:{r0} r1:{r1} c0:{c0} c1:{c1} result:{result}')
                if result <= threshold:
                    highest = max(r1-r0, highest)
                    r1 += 1
                    c1 +=1
                else:
                    r1 -=1
                    c0 +=1
                r1 = max(r0+1,r1)
                c1 = max(c0+1,c1)

        return highest + 1
