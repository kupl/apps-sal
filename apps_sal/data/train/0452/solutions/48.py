class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        memo = {}
        def min_difficulty(i, days_left):
            if (i, days_left) in memo:
                return memo[i, days_left]
            
            if i == len(jobDifficulty):
                if days_left == 0:
                    return 0
                else:
                    return math.inf
            if days_left == 1:
                return max(jobDifficulty[i:])
            
            day_cost = 0
            min_so_far = math.inf
            for j in range(i, len(jobDifficulty)):
                day_cost = max(day_cost, jobDifficulty[j])
                remaining_cost = min_difficulty(j+1, days_left - 1)
                min_so_far = min(min_so_far, day_cost + remaining_cost)
                
            memo[i, days_left] = min_so_far
            return min_so_far
        
        answer = min_difficulty(0, d)
        if answer == math.inf:
            return -1
        else:
            return answer

