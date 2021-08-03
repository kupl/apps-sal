class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        mem = {}
        n = len(jobDifficulty)
        if n < d:
            return -1

        def get_dp(i, j):
            if (i, j) not in mem:
                if j == d:
                    mem[i, j] = max(jobDifficulty[i:])
                else:
                    mem[i, j] = min(max(jobDifficulty[i:i + k]) + get_dp(i + k, j + 1) for k in range(1, n - i - d + j + 1))
            return mem[i, j]
        return get_dp(0, 1)
