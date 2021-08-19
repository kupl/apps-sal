class Solution:

    def minDifference(self, A: List[int]) -> int:
        if len(A) <= 4:
            return 0
        max_vals = [0] * 4
        min_vals = [math.inf] * 4
        for a in A:
            for i in range(4):
                if a > max_vals[i]:
                    max_vals[i + 1:] = max_vals[i:-1]
                    max_vals[i] = a
                    break
            for i in range(4):
                if a < min_vals[i]:
                    min_vals[i + 1:] = min_vals[i:-1]
                    min_vals[i] = a
                    break
        res = math.inf
        for i in range(4):
            res = min(res, max_vals[i] - min_vals[3 - i])
        return res
