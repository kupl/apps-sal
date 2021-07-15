class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        dp = [[0] * (target+1) for _ in range(d+1)]
        dp[0][0] = 1
        for i in range(1, d+1):
            for j in range(1, target+1):
                dp[i][j] = sum(dp[i-1][j-k] for k in range(1, min(f,j)+1) )            
        return dp[-1][-1] % (10**9 + 7)
    
#         if target > d*f:
#             return 0
#         dicti = collections.defaultdict(int)
#         def dice_target(rem_dice, summ):
#             if rem_dice == 0:
#                 return 1 if summ == target else 0
#             if summ > target:
#                 return 0
#             if (rem_dice, summ) in dicti:
#                 return dicti[rem_dice, summ]

#             for i in range(1, f+1):
#                 dicti[rem_dice, summ] += dice_target(rem_dice-1, summ+i)
#             return dicti[rem_dice, summ]
        
        
#         return dice_target(d, 0) % (10**9 + 7)


