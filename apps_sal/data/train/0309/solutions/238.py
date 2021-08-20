class Solution:

    def longestArithSeqLength(self, A: 'List[int]') -> int:
        n = len(A)
        if n == 2:
            return 2
        dic = {0: {0: 1}}
        longest = 0
        for i in range(1, n):
            if i not in dic:
                dic[i] = {0: 1}
            for j in range(i):
                diff = A[i] - A[j]
                if diff not in dic[j]:
                    dic[i][diff] = 2
                else:
                    dic[i][diff] = dic[j][diff] + 1
                longest = max(longest, dic[i][diff])
        return longest
