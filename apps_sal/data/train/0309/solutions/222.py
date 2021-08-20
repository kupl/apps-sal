class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        res = 0
        dic = {}
        for i in range(len(A)):
            dic[i] = {}
            for j in range(i):
                key = A[i] - A[j]
                if key in dic[j]:
                    dic[i][key] = dic[j][key] + 1
                else:
                    dic[i][key] = 2
                res = max(res, dic[i][key])
        return res
