class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        diff_dict = {}
        max_ = 0
        for i in range(len(A)):
            diff_dict[i] = {}
            for j in range(i):
                diff = A[i] - A[j]
                if diff in diff_dict[j]:
                    diff_dict[i][diff] = diff_dict[j][diff] + 1
                else:
                    diff_dict[i][diff] = 1

                max_ = max(max_, diff_dict[i][diff])

        return max_ + 1
