from collections import defaultdict


class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        memo = {}

        def r_search(aindex, bindex):
            if aindex == len(A) or bindex == len(B):
                return 0
            if (aindex, bindex) in memo:
                return memo[aindex, bindex]
            best = 0
            best = max(best, r_search(aindex + 1, bindex))
            best = max(best, r_search(aindex, bindex + 1))
            if A[aindex] == B[bindex]:
                best = max(best, r_search(aindex + 1, bindex + 1) + 1)
            memo[aindex, bindex] = best
            return best
        return r_search(0, 0)
