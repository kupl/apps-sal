class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [0 for i in range(len(arr))]

        def findMaxJumps(i):
            if dp[i] != 0:
                return dp[i]
            else:
                ans = 1
                for j in range(i + 1, min(i + d + 1, len(arr))):
                    if arr[j] >= arr[i]:
                        break
                    ans = max(ans, 1 + findMaxJumps(j))
                for j in range(i - 1, max(i - d, 0) - 1, -1):
                    if arr[j] >= arr[i]:
                        break
                    ans = max(ans, 1 + findMaxJumps(j))
                dp[i] = ans
                return ans
        ans = 1
        for i in range(len(arr)):
            ans = max(ans, findMaxJumps(i))
        return ans
