from itertools import combinations

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) in rating and len(rating) == 3:
            return 0
        else:
            output = list(combinations(rating,3))
            count = len(output)
            for i in output:
                if i[0]<i[1] and i[1]>i[2]:
                    count -= 1
                elif i[0]>i[1] and i[1]<i[2]:
                    count -= 1
            return count

