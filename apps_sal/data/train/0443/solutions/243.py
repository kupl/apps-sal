class Solution:
    def numTeams(self, rating: List[int]) -> int:
        output = 0
        for item in itertools.combinations([x for x in range(len(rating))],3):
            if rating[item[0]] < rating[item[1]] < rating[item[2]] or rating[item[0]] > rating[item[1]] > rating[item[2]]:
                output += 1
        return output
            

