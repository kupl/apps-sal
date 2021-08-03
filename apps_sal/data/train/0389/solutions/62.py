class Solution:
    dp = []

    def is_possible(self, l, actual_sum, index, curr_sum, curr_element_count):
        if index >= len(l):
            return False
        if Solution.dp[curr_element_count][curr_sum] != None:
            return Solution.dp[curr_element_count][curr_sum]
        if curr_element_count != 0 and (actual_sum - curr_sum) / (len(l) - curr_element_count) == curr_sum / curr_element_count:
            print(curr_sum / curr_element_count)
            return True
        Solution.dp[curr_element_count][curr_sum] = self.is_possible(
            l, actual_sum, index + 1, curr_sum + l[index], curr_element_count + 1
        ) or self.is_possible(
            l, actual_sum, index + 1, curr_sum, curr_element_count
        )
        return Solution.dp[curr_element_count][curr_sum]

    def splitArraySameAverage(self, A: List[int]) -> bool:
        if A == None or len(A) <= 1:
            return False
        Solution.dp = [[None] * (sum(A) + 10) for _ in range(len(A) + 1)]
        return self.is_possible(A, sum(A), 0, 0, 0)
