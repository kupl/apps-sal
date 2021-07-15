# Sample [1,2,3,7], max gain at each step: [6, 12, 10, 7, 0]
# for [9,-12,8,12,-12,-16,-13,-11,2,2,-10,-5,13,12,-4,13,4,-4,-16,6,-2,13,-8]
# exp [-7, -12, 0, -4, -16, -4, -20, 12, 23, 21, -7, 27, 32, 19, -5, 24, 11, 7, -18, 17, 11, 13, -8, 0]

class Solution:
    # TLE
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        # remaining total value at each index
        remain = list(itertools.accumulate(stoneValue[::-1]))[::-1]
        
        @lru_cache(None)
        def dp(idx):
            if idx >= len(stoneValue):
                return 0
            return remain[idx] - min(dp(idx+i) for i in range(1,4))
        
        first = dp(0)
        second = remain[0] - first
        # print([dp(i) for i in range(len(stoneValue))])
        return 'Alice' if first > second else 'Tie' if first == second else 'Bob'
        

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        # remaining total value at each index
        remain = list(itertools.accumulate(stoneValue[::-1]))[::-1]
        n = len(stoneValue)
        dp = [0] * (n + 4)
        
        for idx in range(n-1,-1,-1):
            dp[idx] = remain[idx] - min(dp[idx+i] for i in range(1,4))
        
        first = dp[0]
        second = remain[0] - first
        print([dp[i] for i in range(len(stoneValue))])
        return 'Alice' if first > second else 'Tie' if first == second else 'Bob'



