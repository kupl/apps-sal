class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        if d == n:
            return sum(jobDifficulty)

        dp = {}

        def moveOnce(d0, difficultyNow, i0):
            if d0 == d:
                return max(difficultyNow, max(jobDifficulty[i0:]))
            if n - i0 - 1 == d - d0:
                return max(jobDifficulty[i0], difficultyNow) + sum(jobDifficulty[i0 + 1:])

            if (d0, difficultyNow, i0) in dp:
                return dp[(d0, difficultyNow, i0)]

            subAns = min(moveOnce(d0, max(jobDifficulty[i0], difficultyNow), i0 + 1), max(jobDifficulty[i0], difficultyNow) + moveOnce(d0 + 1, jobDifficulty[i0 + 1], i0 + 1))

            dp[(d0, difficultyNow, i0)] = subAns

            return subAns

        return moveOnce(1, jobDifficulty[0], 0)
