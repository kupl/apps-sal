class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dp = [0] * (len(nums)+1)
        acc = [0] * (len(nums)+1)
        sumDict = {0:0}
        for k, ele in enumerate(nums):
            dk = k+1
            acc[dk] = acc[k] + ele
            if acc[dk]-target in sumDict:
                dp[dk] = max(dp[k], dp[sumDict[acc[dk]-target]]+1)
            else:
                dp[dk] = dp[k]
                
            sumDict[acc[dk]] = dk
        
        return dp[len(nums)]

