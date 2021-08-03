class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        run = 1
        last_diff = 0
        last = A[0]
        best = 1
        for a in A[1:]:
            diff = last - a
            if diff == 0:
                run = 1
            elif diff * last_diff < 0:
                run += 1
            else:
                run = 2
            best = max(run, best)
            last_diff = diff
            last = a
        return best
