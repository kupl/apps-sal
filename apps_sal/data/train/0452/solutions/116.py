class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        memo = {}

        def top_down(subsets_remaining, index):
            nonlocal jobDifficulty, n, memo
            if subsets_remaining <= 0:
                return float('inf')
            if subsets_remaining == 1:
                if index < n:
                    return max(jobDifficulty[index:])
                return float('inf')
            if (subsets_remaining, index) in memo:
                return memo[subsets_remaining, index]
            min_difficulty = float('inf')
            for i in range(index, n):
                current_max = max(jobDifficulty[index:i + 1])
                remaining_difficulty = top_down(subsets_remaining - 1, i + 1)
                min_difficulty = min(min_difficulty, current_max + remaining_difficulty)
            memo[subsets_remaining, index] = min_difficulty
            return min_difficulty
        return top_down(d, 0)
