class Solution:
    def mincostTickets(self, arr: List[int], costs: List[int]) -> int:

        dp = [float('inf')] * (len(arr) + 1)
        dp[0] = 0

        for i in range(len(arr)):

            j = i
            prev = dp[i]

            while j < len(arr) and arr[j] < arr[i] + 30:

                if arr[j] == arr[i]:
                    dp[j + 1] = min(dp[j + 1], prev + costs[0], prev + costs[1], prev + costs[2])
                elif arr[j] - arr[i] < 7:
                    dp[j + 1] = min(dp[j + 1], prev + costs[1], prev + costs[2])
                elif arr[j] - arr[i] < 30:
                    dp[j + 1] = min(dp[j + 1], prev + costs[2])

                j += 1

        print(dp)

        return dp[-1]
