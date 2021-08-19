class Solution:
    def maxSumAfterPartitioning(self, nums: List[int], k: int) -> int:
        '''

               v
        [1,30,45,_,_,_,_,????]
        [1,15,7, 9,2,5,10], 2

        dp[i] = max( (windowSize * maxInWindow) + dp[i - windowSize] ) for valid windowSize from 1 to k

        return dp[-1]

        30 + [7] => 37
        1  + [15,7] => 31
        0  + [1,15,7] => 45 <<<<<
        [1,15]
        '''

        dp = [0] * len(nums)

        for i in range(len(nums)):

            # generate all window sizes
            # [1,2,3]
            # if k = 3
            for windowSize in range(1, k + 1):
                startIndex = i - windowSize + 1

                # Bounding Function to make sure that I don't run out of bounds
                if startIndex < 0:
                    break

                #         v
                #           v
                # # [1,15,7,9,2,5,10]

                maxVal = max(nums[startIndex: i + 1])

                currVal = windowSize * maxVal

                currSum = currVal

                if startIndex > 0:
                    currSum += dp[startIndex - 1]

                dp[i] = max(dp[i], currSum)
        return dp[-1]
