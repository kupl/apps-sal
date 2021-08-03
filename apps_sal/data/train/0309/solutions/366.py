class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        if len(A) <= 2:
            return len(A)

        dic = {}

        for idx, val in enumerate(A):
            for j in range(idx + 1, len(A)):
                diff = A[j] - val
                if (diff, idx) in dic:
                    dic[diff, j] = dic[(diff, idx)] + 1
                else:
                    dic[diff, j] = 2
        return max(dic.values())
