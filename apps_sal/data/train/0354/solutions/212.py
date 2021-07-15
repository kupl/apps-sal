from collections import defaultdict
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = pow(10, 9) + 7
        rollMax = [0] + rollMax
        for i in range (len(rollMax)):
            rollMax [i] = min(n, rollMax[i])
        
        cache = defaultdict(int)
        def dp (last, consec, pos):
            if pos == n:
                return 1
            if (last, consec, pos) in cache:
                return cache[(last, consec, pos)]
            ans = 0
            for i in range (1, 7):
                if last == i:
                    if consec < rollMax[i]:
                        ans += dp(i, consec + 1, pos + 1)
                else:
                    ans += dp(i, 1, pos + 1)
            cache[(last, consec, pos)] = ans 
            return ans
        
        return dp(0, 0, 0) % mod
