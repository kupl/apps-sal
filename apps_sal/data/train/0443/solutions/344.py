class Solution:
    def numTeams(self, rating: List[int]) -> int:        
        num_teams = 0
        for i, first_rank in enumerate(rating):
            rest = rating[i+1:]
            for j, second_rank in enumerate(rest):
                if second_rank > first_rank:
                    for k, third_rank in enumerate(rest[j+1:]):
                        if third_rank > second_rank:
                            num_teams += 1
                if second_rank < first_rank:
                    for k, third_rank in enumerate(rest[j+1:]):
                        if third_rank < second_rank:
                            num_teams += 1
        
        return num_teams
