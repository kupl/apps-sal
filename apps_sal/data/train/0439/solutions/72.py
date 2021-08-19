class Solution:

    def __init__(self):
        self.lmemo = {}
        self.gmemo = {}

    def maxTurbulenceSize(self, A: List[int]) -> int:

        def rmtsl(pos):
            if pos not in self.lmemo:
                self.lmemo[pos] = 1 + (rmtsg(pos + 1) if A[pos] < A[pos + 1] else 0)
            return self.lmemo[pos]

        def rmtsg(pos):
            if pos not in self.gmemo:
                self.gmemo[pos] = 1 + (rmtsl(pos + 1) if A[pos] > A[pos + 1] else 0)
            return self.gmemo[pos]
        self.lmemo[len(A) - 1] = self.gmemo[len(A) - 1] = 1
        return max([max(rmtsl(i), rmtsg(i)) for i in range(len(A) - 1, -1, -1)])
