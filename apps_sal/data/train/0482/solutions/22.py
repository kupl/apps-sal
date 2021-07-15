class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        maximum = [[0 for i in range(len(arr))]for j in range(len(arr))]
        for i in range(len(arr)):
            localMaximum = -math.inf
            for j in range(i,len(arr)):
                localMaximum = max(localMaximum,arr[j])
                maximum[i][j] = localMaximum
        dp = [[math.inf for i in range(len(arr))] for j in range(len(arr))]
        for i in range(len(arr)):
            dp[i][i] = 0
        for length in range(1,len(arr)):
            for left in range(len(arr)-length):
                right = left+length
                if length==1:
                    dp[left][right] = arr[left]*arr[right]
                else:
                    for k in range(left,right):
                        dp[left][right] = min(dp[left][right],dp[left][k]+dp[k+1][right]+(maximum[left][k]*maximum[k+1][right]))
        return dp[0][len(arr)-1]
