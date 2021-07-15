class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # dfs TLE
        # use sliding window instead
        # keep moving a window of size n - k along the way
        
        maxSum = sum(cardPoints)
        if len(cardPoints) <= k:
            return maxSum
        
        subSum = 0
        ans = 0
        for i in range(len(cardPoints)):
            subSum += cardPoints[i]
            
            if i + 1 >= (len(cardPoints) - k):
                ans = max(ans, maxSum - subSum)
                subSum -= cardPoints[i - (len(cardPoints) - k - 1)]
        
        return ans

