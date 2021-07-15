class Solution:
    def superEggDrop(self, eggs: int, floors: int) -> int:
        dp = [[0] * (eggs+1) for _ in range(floors+1)]
        currFloor = 0
        
        while dp[currFloor][eggs] < floors:
            currFloor += 1
            for i in range(1 , eggs+1):
                dp[currFloor][i] = dp[currFloor - 1][i-1] + dp[currFloor - 1][i] + 1
                
        return currFloor
