class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        self.memo = {}

        def check(left_days, i):
            ky = (left_days, i)
            if ky in self.memo:
                return self.memo[ky]
            m = n - left_days
            diff = jobDifficulty[i]
            mn = float('inf')
            while i < m:
                diff = max(diff, jobDifficulty[i])
                if left_days > 0:
                    mn = min(mn, diff + check(left_days - 1, i + 1))
                else:
                    mn = diff
                i += 1
            self.memo[ky] = mn
            return mn
        return check(d - 1, 0)
