from itertools import combinations
class Solution:
    
    def numTeams(self, rating: List[int]) -> int:
        ### Store the index in dictionary 
        from itertools import combinations
        output = 0
        for item in combinations([x for x in range(len(rating))],3):
            if rating[item[0]] < rating[item[1]] < rating[item[2]] or rating[item[0]] > rating[item[1]] > rating[item[2]]:
                output += 1
        return output
#         dic = {}
#         for i, x in enumerate(rating):
#             dic[x] = i
#         rating.sort()
#         cnt = 0
#         combinations = list(combinations(rating,3))

#         for comb in combinations:
#             if (dic[comb[0]] < dic[comb[1]] and dic[comb[1]] < dic[comb[2]]) or (dic[comb[0]] > dic[comb[1]] and dic[comb[1]] > dic[comb[2]]):
                
#                 cnt += 1
#         return cnt
    

