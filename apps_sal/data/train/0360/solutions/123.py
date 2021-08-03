class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        sums = [0] * (len(weights) + 1)
        for i in range(len(weights)):
            sums[i + 1] = weights[i] + sums[i]

        def backtracking(i, cap, d):
            if i == len(sums):
                return True
            if sums[-1] - sums[i - 1] > cap * d:
                return False
            j = i
            while j < len(sums):
                if sums[j] - sums[i - 1] > cap:
                    break
                j += 1
            return backtracking(j, cap, d - 1)

        l, h = max(weights), sum(weights)

        while l <= h:
            m = (l + h) // 2
            if backtracking(1, m, D):
                h = m - 1
            else:
                l = m + 1
        return l
