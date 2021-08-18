class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        '''
        For each element, it can either go to the previous group, or start a new group
        dp[i][j] = largest sum before i when last group's size is j, last group's largest value
        '''
        dp = [[(0, 0)] * k for _ in range(len(arr) + 1)]
        for i in range(1, len(arr) + 1):
            for j in range(min(i, k)):
                if j == 0:
                    dp[i][j] = max((dp[i - 1][m][0] + arr[i - 1], arr[i - 1]) for m in range(min(i, k)))
                else:
                    new_max = max(dp[i - 1][j - 1][1], arr[i - 1])
                    dp[i][j] = dp[i - 1][j - 1][0] - j * dp[i - 1][j - 1][1] + new_max * (j + 1), new_max
        return max(dp[-1])[0]
