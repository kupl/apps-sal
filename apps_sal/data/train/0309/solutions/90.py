class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dic = {}
        for i, val2 in enumerate(A[1:], start=1):
            for j, val in enumerate(A[:i]):
                diff = val2 - val
                if (j, diff) in dic:
                    dic[i, diff] = dic[j, diff] + 1
                else:
                    dic[i, diff] = 2

        return max(dic.values())
