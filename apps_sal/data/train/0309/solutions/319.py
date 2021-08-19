class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        res = 0
        dic = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                d = A[j] - A[i]
                if (i, d) in dic:
                    dic[j, d] = dic[i, d] + 1
                else:
                    dic[j, d] = 2
                res = max(res, dic[j, d])
        return res
