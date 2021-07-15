class Solution:
    def stoneGameIII(self, arr: List[int]) -> str:
        ln, dp = len(arr), [float('-inf') for _ in range(len(arr))]
        dp.append(0)
        
        for i in range(ln-1, -1,-1):
            sm =0
            for j in range(i, min(ln, i+3)):
                sm +=arr[j]
                dp[i] = max(dp[i], sm - dp[j+1])
        if dp[0]>0:
            return 'Alice'
        elif dp[0]<0:
            return 'Bob'
        return 'Tie'
