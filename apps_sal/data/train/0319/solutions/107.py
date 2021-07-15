class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        from functools import lru_cache
        @lru_cache(None)
        def dp(index, my_turn):
            if index >= len(stoneValue):
                return 0
            if my_turn:
                rst = float('-inf')
                for i in range(3):
                    rst = max(rst, sum(stoneValue[index:index+i+1]) + dp(index+i+1, False))
                return rst
            
            rst = float('inf')
            for i in range(3):
                rst = min(rst, dp(index+i+1, True))
            return rst
        
        score = dp(0, True) * 2
        if score < sum(stoneValue):
            return 'Bob'
        if score == sum(stoneValue):
            return 'Tie'
        return 'Alice'
