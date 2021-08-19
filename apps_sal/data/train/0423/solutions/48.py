class Solution:
    """

    arr = [1,2,3,4] d = 1

    0 - 1
    1 - 2 - 1 -> 1 += 1


    arr = [1,3,5,7] d = 1

    0: 1
    1: 3 - 1 -> 2 -> 1
    2: 5 - 



    """
    import collections

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_len = 0
        for i in arr:
            dp[i] = dp.get(i - difference, 0) + 1
            max_len = max(max_len, dp[i])
        return max_len
