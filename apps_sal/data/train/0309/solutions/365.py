class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        tracker = {}
        max_length = 1
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                if (diff, j) in tracker:
                    tracker[(diff, i)] = tracker[(diff, j)] + 1
                else:
                    tracker[(diff, i)] = 2
                max_length = max(max_length, tracker[(diff, i)])
        return max_length

