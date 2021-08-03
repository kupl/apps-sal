class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        '''
        - Dynamic programming solution
        - We don't need to keep track of all sums, only of the 
          max sum for each possible remainder (0, 1, 2)


        '''

        max_sums = [0] * 3

        for num in nums:
            for max_sum in max_sums[:]:
                max_sums[(num + max_sum) % 3] = max(max_sum + num, max_sums[(num + max_sum) % 3])

        return max_sums[0]
