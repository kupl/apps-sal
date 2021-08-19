class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        self.cache = {}
        return self.helper(jobDifficulty, d, 0)

    def helper(self, jobDifficulty: List[int], d: int, start: int) -> int:
        if d == 1:
            return max(jobDifficulty[start:])
        if (d, start) not in self.cache:
            self.cache[d, start] = min([max(jobDifficulty[start:end]) + self.helper(jobDifficulty, d - 1, end) for end in range(start + 1, len(jobDifficulty) - d + 2)])
        return self.cache[d, start]
