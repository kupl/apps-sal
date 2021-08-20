class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        dp = [0] * len(arr)
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            dp[i] = dp[i - 1] + arr[i]
        cn = 0
        for i in range(k - 1, len(arr)):
            if i == k - 1:
                if dp[i] // k >= threshold:
                    cn += 1
            elif (dp[i] - dp[i - k]) // k >= threshold:
                cn += 1
        return cn
