class Solution:
    def numTeams(self, rating: List[int]) -> int:
        from itertools import combinations
        
        def satisfies_condition(inp):
            if inp[0] < inp[1] < inp[2] or inp[0] > inp[1] > inp[2]:
                return True
        
        team_count = 0
        for x in list(combinations(rating, 3)):
            team_count += 1 if satisfies_condition(x) else 0
        
        return team_count

