class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [A[0]]

        for i in range(1, len(A)):
            max_partition_sum = A[i] + dp[-1]
            max_element = A[i]
            end = i - K

            if (end < -1):
                end = -1

            for j in range(i - 1, end, -1):
                if (A[j] > max_element):
                    max_element = A[j]

                partition_sum = (i - j + 1) * max_element

                if (j > 0):
                    partition_sum += dp[j - 1]

                if (partition_sum > max_partition_sum):
                    max_partition_sum = partition_sum

            dp.append(max_partition_sum)

        return dp[-1]
