from itertools import combinations
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        indices = list(range(0, len(rating)))
        all_combs = combinations(indices,3)
        result = 0
        for comb in all_combs:
            if comb[0] < comb[1] and comb[1] < comb[2]:
                if rating[comb[0]] < rating[comb[1]] and rating[comb[1]] < rating [comb[2]]:
                    result += 1
                elif rating[comb[0]] >rating[comb[1]] and rating[comb[1]] > rating[comb[2]]:
                    result += 1
        return result
            
        

