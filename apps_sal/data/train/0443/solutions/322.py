class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        
        def dfs(i: int, prefix: List[int], increasing: bool) -> int:
            if len(prefix) == 3: return 1
            if i == len(rating): return 0
            result = 0
            rate = rating[i]
            if (increasing and prefix[-1] < rate) or (not increasing and prefix[-1] > rate):
                result += dfs(i+1, prefix + [rate], increasing)
            result += dfs(i+1, prefix, increasing)
            return result

        
        result = 0
        for i in range(len(rating)):
            result += dfs(i + 1, [rating[i]], True) + dfs(i + 1, [rating[i]], False)
        return result
