class Solution:
    def calc_num_variations(self, num_ones, memo):

        if num_ones in memo:
            return memo[num_ones]

        curr_sum = 0

        for x in range(num_ones + 1):
            curr_sum += x
            if not x in memo:
                memo[x] = curr_sum

        memo[num_ones] = curr_sum

        return curr_sum

    def numSub(self, s: str) -> int:
        memo = {}
        num_ones = 0

        num_variations = 0

        for one in s:
            if one == '1':
                num_ones += 1
            else:
                num_variations += self.calc_num_variations(num_ones, memo)
                num_ones = 0

        if num_ones > 0:
            num_variations += self.calc_num_variations(num_ones, memo)

        return num_variations % (10**9 + 7)
