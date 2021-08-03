class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)  # Longest subseq that ends with they key.
        for i, elem in enumerate(arr):
            dp[elem] = 1 + dp[elem - difference]

        maxElem = 0
        for key in dp:
            maxElem = max(maxElem, dp[key])

        return maxElem
