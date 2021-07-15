class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        m = {0:False, 1:True}
        def helper(n):
            if n in m:
                return m[n]
            ans, start = False, 1
            while start*start<=n:
                ans = ans or (not helper(n-start*start))
                if ans:
                    m[n]=ans
                    return ans
                start+=1
            m[n]=ans
            return ans
        
        return helper(n)

