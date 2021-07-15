import numpy as np

class Solution:
    def racecar(self, target: int) -> int:
        def dp(t):
            if ans[t] > 0:
                return ans[t]
            n = int(np.ceil(np.log2(t + 1)))
            if 1 << n == t + 1:
                ans[t] = n
                return ans[t]
            ans[t] = n + 1 + dp((1 << n) - 1 - t)
            for m in range(n):
                cur = (1 << (n - 1)) - (1 << m)
                ans[t] = min(ans[t], n + m + 1 + dp(t - cur))
            return ans[t]
            
        ans = [0 for _ in range(target + 1)]
        return dp(target)
