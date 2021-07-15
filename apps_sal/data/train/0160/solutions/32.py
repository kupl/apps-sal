class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
#         alex = [[0 for x in range(2)] for y in range((len(piles)//2)+1)]
#         lee = [[0 for x in range(2)] for y in range((len(piles)//2)+1)]
#         first,last = 0,len(piles)-1
#         turn = 0
#         x,y = 1,1
#         while first < last:
#             if turn == 0:
#                 alex[x][0] = max(alex[x-1][0],alex[x-1][1]) + first
#                 alex[x][1] = max(alex[x-1][0],alex[x-1][1]) + last
            
        dp = [[-1 for x in range(len(piles))] for y in range(len(piles))]
        def recur_dp(si,ei,turn):
            if si > ei:
                return 0
            if dp[si][ei] != -1:
                return dp[si][ei]
            if turn == 0: #alex turn
                start = recur_dp(si+1,ei,1 - turn) + piles[si]
                end = recur_dp(si,ei-1,1-turn) + piles[ei]
                dp[si][ei] = max(start,end)
                return dp[si][ei]
            else:
                start = recur_dp(si+1,ei,1-turn) - piles[si]
                end = recur_dp(si,ei-1,1-turn) - piles[ei]
                dp[si][ei] = min(start,end)
                return dp[si][ei]
        recur_dp(0,len(piles)-1,0)
        return dp[0][len(piles)-1] >= 0
            
        

