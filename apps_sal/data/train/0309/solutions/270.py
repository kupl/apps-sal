class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [{} for _ in range(n)]
        result = 2

        for i in range(1, n):
            for j in range(i):
                delta = nums[i] - nums[j]
                longestArithSeq = 2

                if delta in dp[j]:
                    longestArithSeq = dp[j].get(delta) + 1

                dp[i][delta] = longestArithSeq

                result = max(result, longestArithSeq)

                if result == 3:
                    print('dim')

        return result
