class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.dp = [[None for i in range(len(piles))] for i in range(len(piles))]
        self.func(piles, 0, 0, len(piles)-1, 0, 0)
        return self.dp[0][len(piles)-1]
    
    
    def func(self, arr, turn, i, j, a, b):
        if self.dp[i][j] == True:
            return True
        elif self.dp[i][j] == False:
            return False

        if  i == j:
            b += arr[i]
            self.dp[i][j] = a > b
            return self.dp[i][j]

        if not turn:
            self.dp[i][j] = self.func(arr, turn^1, i+1, j, a+arr[i], b) or self.func(arr, turn^1, i, j-1, a+arr[j], b)
            return self.dp[i][j]
        else:
            self.dp[i][j] = self.func(arr, turn^1, i+1, j, a, b+arr[i]) or self.func(arr, turn^1, i, j-1, a, b+arr[j])
            return self.dp[i][j]
    
    
        
    # Gives TLE
    # def recur(self, arr, turn, a, b):
    #     if len(arr) == 1:
    #         b += arr[0]
    #         return a > b
    #     if not turn:
    #         return self.recur(arr[1:], turn^1, a+arr[0], b) or self.recur(arr[:-1], turn^1, a+arr[-1], b)
    #     else:
    #         return self.recur(arr[1:], turn^1, a, b+arr[0]) or self.recur(arr[:-1], turn^1, a, b+arr[-1])

