class Solution:
    def numTeams(self, rating: List[int]) -> int:

        
        count = 0
        
        for i in range(len(rating)):
            map_g = {}
            map_l = {}
            for j in range(i + 1, len(rating)):
                count += sum([k < rating[j] for k in list(map_l.keys())])+ sum([k > rating[j] for k in list(map_g.keys())])
                if rating[i] < rating[j]:
                    map_l[rating[j]] = map_l.get(rating[j], 0) + 1
                if rating[i] > rating[j]:
                    map_g[rating[j]] = map_g.get(rating[j], 0) + 1
        return count

