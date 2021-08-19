class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        d = {}
        dd = [{} for i in range(len(A))]
        m = 0
        for i in range(len(A)):

            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                # if diff not in d:
                #    d[diff] = 0
                if diff not in dd[i]:
                    dd[j][diff] = 1
                else:
                    dd[j][diff] = dd[i][diff] + 1

                if dd[j][diff] > m:
                    m = dd[j][diff]

                #d[diff] += 1
        # if not d:
        #    return 0
        # print(d)
        # return max(d.values()) + 1
        return m + 1
