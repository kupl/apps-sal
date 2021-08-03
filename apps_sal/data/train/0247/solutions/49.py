class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        record = collections.defaultdict()
        record[0] = 0
        l1 = l2 = float('Inf')
        tmp_sum = 0
        res = float('Inf')
        dp = [float('Inf') for _ in range(len(arr))]
        for i in range(len(arr)):
            tmp_sum += arr[i]
            if tmp_sum - target in record:
                dp[i] = i - record[tmp_sum - target] + 1
            record[tmp_sum] = i + 1
            if i > 0:
                dp[i] = min(dp[i], dp[i - 1])

        record.clear()
        tmp_sum = 0
        record[0] = len(arr)
        for i in range(len(arr) - 1, 0, -1):
            tmp_sum += arr[i]
            if tmp_sum - target in record:
                res = min(res, dp[i - 1] + record[tmp_sum - target] - i)
            record[tmp_sum] = i

        return res if res < float('Inf') else -1
