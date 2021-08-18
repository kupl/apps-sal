class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:

        self.answer = {}

        def max_starting_i(index_A):
            array = A[index_A:]
            if index_A in self.answer:
                return self.answer[index_A]
            if len(array) == 0:
                self.answer[index_A] = 0
                return 0
            if len(array) <= K:
                self.answer[index_A] = max(array) * len(array)
                return self.answer[index_A]
            max_start_here = 0
            for i in range(0, K):
                max_split_here = (i + 1) * max(array[:i + 1]) + max_starting_i(index_A + i + 1)
                max_start_here = max(max_start_here, max_split_here)
            self.answer[index_A] = max_start_here
            return max_start_here

        return max_starting_i(0)
