class Solution:
    def solve(self, start_index, num_groups):
        if (start_index, num_groups) in self.memo:
            return self.memo[(start_index, num_groups)]

        if start_index == 0:
            sum_up_to = 0
        else:
            sum_up_to = self.sums[start_index - 1]

        if num_groups == 1:
            res = (self.sums[-1] - sum_up_to) / (self.N - start_index)
        else:
            res = 0
            num_remaining_groups = num_groups - 1
            for start_next_group in range(start_index + 1, self.N - num_remaining_groups + 1):
                group_avg = (self.sums[start_next_group - 1] - sum_up_to) / (start_next_group - start_index)
                res = max(res, group_avg + self.solve(start_next_group, num_groups - 1))
                pass

        self.memo[(start_index, num_groups)] = res
        return res

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        self.memo = {}  # start index, K -> result

        self.N = len(A)
        self.sums = [None] * len(A)
        self.sums[0] = A[0]
        for i in range(1, len(A)):
            self.sums[i] = self.sums[i - 1] + A[i]

        r = self.solve(0, K)
        print(self.memo)
        return r
