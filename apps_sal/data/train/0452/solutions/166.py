class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(maxsize=None)
        def helper(i, d):
            if d == 1:
                return max(jobDifficulty[i::])
            if len(jobDifficulty)-i < d or d == 0:
                return -1
            if len(jobDifficulty)-i == d:
                return sum(jobDifficulty[i::])
            tans = 2**64
            max_d = jobDifficulty[i]
            for j in range(0, len(jobDifficulty)-i-d+1):
                max_d = max(max_d, jobDifficulty[i+j])
                tans = min(helper(i+j+1, d-1)+max_d, tans)
            return tans                
        return helper(0, d)

