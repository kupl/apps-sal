class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        dp = [float('inf') for i in range(len(arr))]
        curr_sum = 0
        hist = {0: -1}
        res = float('inf')
        shortest_length = float('inf')
        for i, num in enumerate(arr):
            curr_sum += num
            diff = curr_sum - target
            if diff in hist:
                index = hist[diff]
                length = i - index
                # print(i, index)
                if index > 0 and dp[index] != float('inf'):
                    res = min(res, dp[index] + length)
                shortest_length = min(shortest_length, length)
            hist[curr_sum] = i
            dp[i] = shortest_length
        # print(dp)
        return res if res != float('inf') else -1
