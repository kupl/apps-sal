class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        # we can use memoization
        DP = {}
        def get_rolls(n, t):
            if n == 1:
                if 0 < t <= f:
                    return 1
                return 0
            if (n, t) in DP:
                return DP[(n, t)]
            
            total = 0
            
            for i in range(1, f+1):
                total += get_rolls(n-1, t-i)
            
            DP[(n, t)] = total
            return total
        
        return get_rolls(d, target) % (10**9 + 7)
