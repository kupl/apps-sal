class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        dict = collections.defaultdict(lambda: 0)

        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                dict[(j, A[j] - A[i])] = dict.get((i, A[j] - A[i]), 1) + 1

        return max(dict.values())
