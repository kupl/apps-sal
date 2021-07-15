class Solution:
    res = 0
    def numTeams(self, rating: List[int]) -> int:
        
        def dfs(rating, start, prev):
            if len(prev) == 3:
                self.res += 1
                return
            for i in range(start, len(rating)):
                if not prev or prev[-1] < rating[i]:
                    dfs(rating, i+1, prev + [rating[i]])
        
        dfs(rating, 0, [])
        dfs(rating[::-1], 0, [])
        return self.res

