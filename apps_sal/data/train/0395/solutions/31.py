from sortedcontainers import SortedList


class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        sl = SortedList()
        dp = [[False, False] for _ in range(len(A))]
        prev_idx = dict()
        dp[-1] = [True, True]
        for i in range(len(A) - 1, -1, -1):
            if i < len(A) - 1:
                (l, r) = (sl.bisect_left((A[i], float('inf'))), sl.bisect_right((A[i], float('-inf'))))
                if l > 0:
                    dp[i][1] = dp[sl[l - 1][1]][0]
                if r < len(sl):
                    dp[i][0] = dp[sl[r][1]][1]
            if A[i] in prev_idx:
                sl.discard((A[i], prev_idx[A[i]]))
            sl.add((A[i], i))
            prev_idx[A[i]] = i
        return sum((odd == True for (odd, even) in dp))
