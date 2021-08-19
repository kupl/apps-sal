from collections import Counter


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        c = dict(Counter(A).most_common())
        # print(c)
        m1 = max(c.values())
        # A = list(set(A))
        # A.sort()
        index = {}
        # for i in range(len(A)):
        # index[A[i]]=i
        dp = [[2] * len(A) for i in A]
        m = 2
        for i in range(len(A)):
            # print(\"I=\", i)
            # index[A[i+1]]=(i+1)
            for j in range(i + 1, len(A)):
                # index[A[j]]=(j)
                a = A[i]

                c = A[j]
                b = 2 * a - c
                # print(b,a,c)
                if b in index:
                    # print(\"B {} in index \".format(b))
                    # print(b,a,c,i,j)
                    dp[i][j] = dp[index[b]][i] + 1
            index[A[i]] = i
            m = max(m, max(dp[i]))
        # # print(A)
        # for i,d in enumerate(dp):
        #     print(A[i],d)
        return max(m, m1)
