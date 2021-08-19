class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import defaultdict
        opt = defaultdict(lambda: defaultdict(int))
        l = len(A)
        sol = 0
        for i in range(l):
            for j in range(i + 1, l):
                diff = A[j] - A[i]
                sub_l = 2
                if diff in opt[i]:
                    sub_l = opt[i][diff] + 1
                opt[j][diff] = max(opt[j][diff], sub_l)
                sol = max(sol, opt[j][diff])
        return sol
