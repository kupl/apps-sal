class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # DP?
        if len(A) <= 2:
            return len(A)
        DP = [{} for i in range(len(A))]
        ret = 0
        for i in range(1, len(A)):
            # j < i
            for j in range(i):
                diff = A[i] - A[j]
                l = 0
                if diff in DP[j]:
                    l = DP[j][diff] + 1
                else:
                    l = 2  # A[j] and A[i]
                new_longest = max(l, DP[i].get(diff, 0))
                ret = max(ret, new_longest)
                DP[i][diff] = new_longest
        return ret
