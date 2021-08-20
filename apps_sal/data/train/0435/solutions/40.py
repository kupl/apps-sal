class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        """
        #Running sum
        a - b = n * k, a is curr_sum, b is prev_sum
        We're looking for prev_sum that can add a to -> looking for b
        b = a - n * k 
        b % k = a % k
        -> see if running total % k -> find the prev_sum % k

        """
        dp = [1] + [0] * K
        result = 0
        running_sum = 0
        for num in A:
            running_sum += num
            result += dp[running_sum % K]
            dp[running_sum % K] += 1
        return result
