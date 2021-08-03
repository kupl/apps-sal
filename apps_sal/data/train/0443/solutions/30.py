class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        if len(rating) > 2:
            for i in rating[:-2]:
                for j in rating[(rating.index(i) + 1):-1]:
                    for k in rating[(rating.index(j) + 1):]:
                        if (i < j) and (j < k):
                            count += 1
                        elif (i > j) and (j > k):
                            count += 1
                        else:
                            count += 0
        else:
            count = 0
        return count
