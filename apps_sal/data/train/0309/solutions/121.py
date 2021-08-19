class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        res = 0
        dic = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                d = A[j] - A[i]
                dic[j, d] = dic.get((i, d), 1) + 1
        return max(dic.values())
