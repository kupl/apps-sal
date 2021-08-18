class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        dp = [0 for i in range(len(arr))]
        dp[0] = (1, 0) if arr[0] % 2 == 1 else (0, 1)
        for i in range(1, len(dp)):
            if arr[i] % 2 == 0:
                oddCount = dp[i - 1][0]
                evenCount = dp[i - 1][1] + 1
            else:
                oddCount = dp[i - 1][1] + 1
                evenCount = dp[i - 1][0]
            dp[i] = (oddCount, evenCount)
        return sum([elem[0] for elem in dp]) % (10**9 + 7)
