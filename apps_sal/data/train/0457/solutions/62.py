class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_mat = [-1] * (amount + 1)
        dp_mat[0] = 0

        for i in range(1, amount + 1):
            min_num = None
            
            for denom in coins:
                if denom <= i and dp_mat[i - denom] != -1:
                    temp = 1 + dp_mat[i - denom]
                    if not min_num:
                        min_num = temp
                    elif temp < min_num:
                        min_num = temp
            
            if min_num:
                dp_mat[i] = min_num
        
        return dp_mat[-1]

