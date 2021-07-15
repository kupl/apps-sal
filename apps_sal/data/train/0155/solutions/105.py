class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = {}
        
        def jump(i):
            
            if i in dp:
                return dp[i]
            
            m = 1
            step = 1
            while i + step < len(arr) and step <= d:
                if arr[i] <= arr[i + step]:
                    break
                m = max(m, jump(i + step) + 1)
                step += 1
         
            step = 1
            while i - step >= 0 and step <= d:
                if arr[i] <= arr[i - step]:
                    break
                m = max(m, jump(i - step) + 1)
                step += 1
            
            dp[i] = m
            return m
        
        ans = 0
        for i in range(len(arr)):
            if i not in dp:
                jump(i)
            ans = max(ans, dp[i])
        return ans
