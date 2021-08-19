class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        convert this into a sliding window problem
        rephrase the problem:
            find the max window of length k between cardPoints[n-k:n+k]
        [1,2,3,4,5,6]
        k = 2
        4,5,0,1


        """
        ans = 0
        curSum = 0
        n = len(cardPoints)
        for i in range(n - k, n + k):
            curSum += cardPoints[i % n]
            if i >= n:
                curSum -= cardPoints[(i - k) % n]
            ans = max(ans, curSum)
        return ans
