class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        arr = stoneValue[:]
        dp = [0 for _ in range(3)]
        
        for i in range(len(arr)-1, -1, -1):
            dp[i%3] = max(sum(arr[i:i+k])- dp[(i+k)%3] for k in range(1, 4))
        return 'Alice' if dp[0] > 0 else 'Bob' if dp[0] <0 else 'Tie'

