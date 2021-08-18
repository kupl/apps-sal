class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        prefix_sum, current_sum = [], 0

        for num in A:
            current_sum += num
            prefix_sum.append(current_sum)

        i, j = -1, L - 1
        max_m, sub = float('-inf'), 0
        sum_l, max_tot = 0, 0
        while j < len(prefix_sum):
            sum_l = prefix_sum[j] - sub
            sum_m = max(self.findM(prefix_sum[:i + 1], M, 0), self.findM(prefix_sum[j + 1:], M, prefix_sum[j]))
            max_tot = max(max_tot, sum_m + sum_l)
            i += 1
            j += 1
            sub = prefix_sum[i]

        return max_tot

    def findM(self, prefix_sum, M, sub):
        if not prefix_sum or len(prefix_sum) < M:
            return 0
        max_m = float('-inf')
        sum_m = 0
        i, j = -1, M - 1
        while j < len(prefix_sum):
            sum_m = (prefix_sum[j] - sub)
            i += 1
            j += 1
            sub = prefix_sum[i]
            max_m = max(sum_m, max_m)
        return max_m
