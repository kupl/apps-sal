class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        self.results = {}
        self.results[len(A) - 1] = {}
        for i in range(len(A) - 2, -1, -1):
            self.results[i] = {}
            for j in range(i + 1, len(A), 1):
                diff = A[i] - A[j]
                possibility = self.results[j].get(diff, 1)
                if 1 + possibility > self.results[i].get(diff, 0):
                    self.results[i][diff] = 1 + possibility
        result = 1
        for i in range(0, len(A) - 1, 1):
            for value in list(self.results[i].values()):
                result = max(result, value)
        return result
