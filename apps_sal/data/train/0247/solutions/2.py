class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1

        def getMinSub(arr, target):
            dp = [float('inf')] * len(arr)
            total = 0
            lookup = defaultdict(int)
            for index, val in enumerate(arr):
                total += val
                if total == target:
                    dp[index] = index - 0 + 1
                elif total - target in lookup:
                    dp[index] = min(index - lookup[total - target] + 1, dp[index - 1])
                else:
                    dp[index] = dp[index - 1]

                lookup[total] = index + 1
            return dp

        forward = getMinSub(arr, target)
        backward = getMinSub(arr[::-1], target)[::-1]

        minresult = float('inf')
        for i in range(1, len(arr)):
            minresult = min(minresult, forward[i - 1] + backward[i])

        return minresult if minresult != float('inf') else -1
