class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dict1 = {}
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                dict1[(A[j] - A[i], j)] = dict1.get((A[j] - A[i], i), 1) + 1
        return max(dict1.values())

